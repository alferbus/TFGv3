# -*- coding: utf-8 -*-
import os,time,obd
from gps3.agps3threaded import AGPS3mechanism
from PyQt4 import QtCore, QtGui
from UI import PIDshow
from data import DataManagement
from OnlineDialog import OnlineDialog
#TODO: Wrapper class for user_list, car_list, pid_list. 

class PidShowDialog(QtGui.QDialog):
	def __init__(self,obd_path,user_data,user_index,car_index,current_pid_name,parent=None):
		QtGui.QWidget.__init__(self, parent)
		
		#------------------------ UI SETUP -----------------------------
		self.ui = PIDshow.Ui_Dialog() # this brings up the GUI built with QtDesigner
		self.ui.setupUi(self)
		self.setWindowFlags(
			QtCore.Qt.FramelessWindowHint) # remove the window frame
			# ~ | QtCore.Qt.WindowStaysOnTopHint) # keep the focus
		self.setAttribute(QtCore.Qt.WA_DeleteOnClose,True) # delete dialog on close
		#-------------------------- USER DATA --------------------------
		self.uindex = 	user_index
		self.cindex = 	car_index		
		self.data = 	user_data
		
		self.obd_path = obd_path
		#---------------------------------------------------------------
		self.connect(
			self.ui.pushButtonBack, QtCore.SIGNAL('clicked()'),self.back)
		self.connect(
			self.ui.pushButtonStart, QtCore.SIGNAL('clicked()'),self.online_pressed)
		#-------------------- THREAD MANAGEMENT ------------------------
			
		self.workerThread = WorkerThread(self.obd_path,user_data,user_index,
		car_index,current_pid_name)
		
		self.connect(self.workerThread, QtCore.SIGNAL("valueUpdate(QString)"),
			self.valueUpdate,QtCore.Qt.DirectConnection)
		
		self.ui.labelPid.setText(current_pid_name)
		self.workerThread.start()
		
	def valueUpdate(self,value):
		#update label with new data
		#grab self.selected_pid_name and value as arguments passed.
		self.ui.labelValue.setText(value)
		
	def back(self):
		self.ui.pushButtonBack.setFlat(True)
		self.ui.pushButtonBack.setText(u"Saliendo...")
		self.workerThread.stop_polling()
		self.workerThread.close_online()
		self.workerThread.terminate()
		
		from PidSelectDialog import PidSelectDialog
		pid_select = PidSelectDialog(self.obd_path,self.data,self.uindex,self.cindex)
		self.close()
		pid_select.exec_()
	
	def online_pressed(self):
		self.workerThread.display_online()
		
class WorkerThread(QtCore.QThread):
	def __init__(self,obd_path,user_data,user_index,car_index,current_pid_name,
	parent=None):
		super(WorkerThread,self).__init__(parent)
		
		self.uindex = 	user_index
		self.cindex = 	car_index
		self.obd_path = obd_path
				
		self.data = 	user_data
		self.username = self.data.user_list[self.uindex]['name']
		self.car =		self.data.car_list[self.cindex]['maker']
		self.database = DataManagement(self.username,self.car,self.uindex,self.cindex,self.data)
				
		self.selected_pid_name = current_pid_name
		self.l = [] #set empty writelist buffer (items to be written on DB)
		self.sample_number = 1 #sample number
		
		self.start_gps()
		self.connection = obd.OBD(self.obd_path)
		self.poll = True
		self.online = OnlineDialog(self.data,self.cindex)
		self.online_commands = ['RPM','THROTTLE_POS','SPEED']
		self.online_results = []
		
	def close_online(self):
		self.online.setAttribute(QtCore.Qt.WA_DeleteOnClose,True) 
		self.online.terminate_thread()
		self.online.close()
		
	def stop_polling(self):
		self.poll = False
	def display_online(self):
		self.online.exec_()
	def start_gps(self):
		"""GPS FIX"""
		#R-pi GPSD needs to be disabled as well:
		os.system('sudo systemctl stop gpsd.socket')
		os.system('sudo systemctl disable gpsd.socket')
		#Check if the fix is ready:
		#TODO: MENSAJE: espere al fix del GPS. Quitar boton de comenzar y dejar sólo el
		#de ir atrás
		try:
			self.agps_thread = AGPS3mechanism()  # Instantiate AGPS3 Mechanisms
			self.agps_thread.stream_data()  # From localhost (), or other hosts, by example, (host='gps.ddns.net')
			self.agps_thread.run_thread()  # Throttle time to sleep after an empty lookup, default '()' 0.2 two tenths of a second
		except (OSError, IOError):
			mb = QtGui.QMessageBox (
			u'Advertencia',u'Compruebe la conexión del GPS',
			QtGui.QMessageBox.Warning,QtGui.QMessageBox.Ok,0,0)
			mb.setWindowFlags(QtCore.Qt.FramelessWindowHint)
			mb.setAttribute(QtCore.Qt.WA_DeleteOnClose,True) # delete dialog on close
			mb.exec_() #prevent focus loss
			raise SystemExit #No gps device found -- QUIT
	def gps_check(self):
		#Check the gps stream and sample time,latitude,longtide and speed
		#from satellites
		try:
			while(True):		
				if self.agps_thread.data_stream.lat != 'n/a':
					self.l.append(self.sample_number)
					self.l.append(self.agps_thread.data_stream.time)
					self.l.append(self.agps_thread.data_stream.lat)
					self.l.append(self.agps_thread.data_stream.lon)
					self.l.append(self.agps_thread.data_stream.speed)
					break
			#~ if self.agps_thread.data_stream.time != self.l[1]:
				#~ break
		except (OSError, IOError):
			mb = QtGui.QMessageBox (
			u'Advertencia',u'Compruebe la conexión del GPS',
			QtGui.QMessageBox.Warning,QtGui.QMessageBox.Ok,0,0)
			mb.setWindowFlags(QtCore.Qt.FramelessWindowHint)
			mb.setAttribute(QtCore.Qt.WA_DeleteOnClose,True) # delete dialog on close
			mb.exec_() #prevent focus loss
			raise SystemExit #No gps device found -- QUIT
		finally:
			self.sample_number+=1
			self.update_label() #If new GPS data is available
								#(= at least one second has gone by)
								#then car is queried for new obd data
	def update_label(self):
		#------------------------ SHOW SELECTED PID --------------------
		c = obd.commands[self.selected_pid_name]
		r = self.connection.query(c)
		try:
			self.value = str(r.value.magnitude)
		except AttributeError as e:
			self.value = str(r.value)
		#~ self.ui.labelValue.setText(value)
		#------------------------ CHECK THE OTHER PIDS -----------------
		pid_list = self.data.pid_list[self.cindex]
		#------------------------ ONLINE PIDS --------------------------
		for o in self.online_commands:
			c = obd.commands[o]
			r = self.connection.query(c)
			try:
				self.online_results.append(r.value.magnitude)
			except AttributeError as ae:
				self.online_results.append(str(r.value))
		#---------------------------------------------------------------
		self.online_results[0] = int(self.online_results[0])
		self.online_results[1] = float(self.online_results[1])
		self.online_results[2] = float(self.online_results[2])
		
		self.online.set_online(self.online_results)
		self.online_results = []
		#---------------------- USER-SELECTED PIDS ---------------------
		for a_pid in pid_list:
			pid_name = self.data.pid_list[self.cindex][a_pid]
			c = obd.commands[pid_name]
			r = self.connection.query(c)
			try:
				self.l.append(r.value.magnitude)
			except AttributeError as ae:
				self.l.append(str(r.value))
		#~ print self.l
		self.database.write(self.l)
		#-------------------------------------
		self.l = [] #purge writelist buffer	def start_gps(self):

	def run(self):
		while self.poll == True:
			self.gps_check()
			time.sleep(1)
			self.value = QtCore.QString(self.value)
			self.emit(QtCore.SIGNAL("valueUpdate(QString)"),self.value) #custom signal
