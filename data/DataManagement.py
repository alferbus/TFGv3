# -*- coding: utf-8 -*-
from datetime import datetime
import sqlite3
import os

class DataManagement(object):
	def __init__(self,username,car,user_index,car_index,userdata):
		#---------------------------- DB-CREATOR ----------------------- 
		today = unicode(datetime.now()) #get today's date
		try:
			os.makedirs('users/'+username)
		except OSError: #folder already exists, do nothing then.
			pass
		now = datetime.now() #get today's date
		filename = unicode(username)+u'_'+unicode(car)+u'_'+unicode(now.year)+u'.'+unicode(now.month)+u'.'+unicode(now.day)+u'_'+unicode(now.hour)+u'.'+unicode(now.minute)+u'.'+unicode(now.second)+u'.db'
		self.__path = u'users/'+username+u'/'+filename
		self.data = userdata
		self.uindex = user_index
		self.cindex = car_index
		self.columns = self.data.pid_list[self.cindex].values()
		
		conn = sqlite3.connect(self.__path) 
		cursor = conn.cursor()
		cursor.execute("""
			CREATE TABLE 'session' (
				'SAMPLE'	INTEGER,
				'DATE'      TEXT,
				'LATITUDE'  REAL,
				'LONGITUDE'	REAL,
				'GPS_SPEED'	REAL
			);""")
		for new_column in self.columns:
			cursor.execute("ALTER TABLE session ADD COLUMN "+new_column+" REAL;")
			
		conn.commit()
		conn.close()
	def write(self,l):
		conn = sqlite3.connect(self.__path) 
		cursor = conn.cursor()
		
		cursor.execute("""INSERT INTO session 
		(SAMPLE,DATE,LATITUDE,LONGITUDE,GPS_SPEED)
		VALUES (?,?,?,?,?);""",(l[0],l[1],l[2],l[3],l[4]))
		i=1
		for COLUMN in self.columns:
			SAMPLE = l[0]
			datum = l[4+i]
			try:
				VALUE = float(datum)
			except ValueError:
				VALUE = 0.0
			cursor.execute("UPDATE session SET "+str(COLUMN)+" = "+str(VALUE)+" WHERE SAMPLE = "+str(SAMPLE)+";")
			i+=1
		#~ obd_values = l[4:]
		#~ for datum in obd_values:
			#~ SAMPLE = l[0]
			#~ COLUMN = self.columns[i]
			#~ if datum == 'None':
				#~ VALUE = 0
			#~ else:
				#~ VALUE = datum
			#~ cursor.execute("UPDATE session SET "+str(COLUMN)+" = "+str(VALUE)+" WHERE SAMPLE = "+str(SAMPLE)+";")
			#~ i+=1

		conn.commit()
		conn.close()
	def obd_write(self,l):
		pass
		#~ conn = sqlite3.connect(self.__path) 
		#~ cursor = conn.cursor()
		#~ i = 5
		
		#~ for column in self.columns:
			#~ cursor.execute("""INSERT INTO session (?)
			#~ VALUES (?);""",(column,l[5]))
			#~ l+=1
		#~ conn.commit()
		#~ conn.close()
