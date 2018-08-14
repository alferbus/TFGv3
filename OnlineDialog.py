# -*- coding: utf-8 -*-
import os,time,obd,numpy
from gps3.agps3threaded import AGPS3mechanism
from PyQt4 import QtCore, QtGui
from UI import online
#TODO: Wrapper class for user_list, car_list, pid_list. 

class OnlineDialog(QtGui.QDialog):
	def __init__(self,user_data,cindex,parent=None):
		QtGui.QWidget.__init__(self, parent)
		
		self.data 		= user_data
		self.cindex 	= cindex
		self.car_type 	= self.data.car_list[self.cindex]['fuel']
		#------------------------ UI SETUP -----------------------------
		self.ui = online.Ui_Dialog() # this brings up the GUI built with QtDesigner
		self.ui.setupUi(self)
		self.setWindowFlags(
			QtCore.Qt.FramelessWindowHint) # remove the window frame
			# ~ | QtCore.Qt.WindowStaysOnTopHint) # keep the focus
		#~ self.setAttribute(QtCore.Qt.WA_DeleteOnClose,True) # delete dialog on close
		
		#---------------------------------------------------------------
		self.connect(
			self.ui.pushButtonBack, QtCore.SIGNAL('clicked()'),
			self.back)
		
		self.dialogThread =  DialogThread(self.car_type)
		self.connect(self.dialogThread, QtCore.SIGNAL("onlineUpdate(QStringList)"),
			self.update_online,QtCore.Qt.DirectConnection)
	
	def terminate_thread(self):
		self.dialogThread.terminate()
		
	def back(self):
		self.hide()
	
	def set_online(self,values):
		if self.dialogThread.thread_running == False:
			self.online_results = values
			self.dialogThread.set_values(values)
			self.dialogThread.set_running(True)
			self.dialogThread.start()
		else:
			self.online_results = values
			self.dialogThread.set_values(values)
	
	def update_online(self,values):
		#~ print "*************"
		#~ print "DEV: {}, RPM: {} , THROTTLE: {}".format(values[0],values[1],values[2])
		#~ print "*************"
		self.ui.labelDevValue.setText(values[0])
		self.ui.labelRPMValue.setText(values[1])
		self.ui.labelAccValue.setText(values[2])
		self.ui.labelStartValue.setText(values[3])
		self.ui.labelStopValue.setText(values[4])

class DialogThread(QtCore.QThread):
	def __init__(self,car_type,parent=None):
		super(DialogThread,self).__init__(parent)
		self.car_type = car_type
		self.values = [0,0,0,0,0]
		self.previous_values = [0,0,0,0,0]
		self.thread_running = False
		
		self.rpm_w = 0
		self.throttle_w = 0
		self.start_w = 0
		self.stop_w = 0
		self.dev_w = 0
		
		self.w_history= QtCore.QStringList()
		
		self.speed_history = []
		self.dev = 0
		self.start_count = 0
		self.stop_time = 0
		
		
	def set_values(self,values):
		self.previous_values = self.values
		self.values = values
	
	def set_running(self,value):
		self.thread_running = value
		
	def run(self): #[dev,rpm,throttle,start,stop]
		while self.thread_running == True:
			self.w_history = []
			if self.car_type == 'gas':
				lower_limit = 1300
				upper_limit = 2000
			elif self.car_type == 'diesel':
				lower_limit = 1500
				upper_limit = 2500
			self.speed_history.append(self.values[2])
			
			if len(self.speed_history) > 240:
				#~4 samples/s in 5 s = 20 samples
				self.speed_history = self.speed_history[4:]#remove oldest 4 samples
			self.dev = numpy.std(self.speed_history)
			self.dev = round(self.dev,2)
			self.w_history.append(QtCore.QString(str(self.dev)))
			
			if (self.values[0] < lower_limit) or (self.values[0] > upper_limit):
				self.rpm_w += 1
			self.w_history.append(QtCore.QString(str(self.rpm_w)))
			
			if (self.values[1] > 70.0):
				self.throttle_w += 1
			self.w_history.append(QtCore.QString(str(self.throttle_w)))
			
			if (self.values[2] >= 50.0):
				self.start_count = 0
				self.w_history.append(QtCore.QString(str(self.start_w)))
			elif (self.values[2] < 50.0 and self.previous_values[2] != 0):
				self.start_count += 1
				if(self.start_count == 5):
					self.start_w += 1
					self.w_history.append(QtCore.QString(str(self.start_w)))
					self.start_count = 0
			
			if (self.previous_values[2] > self.values[2]):
				self.stop_time += 1
				if(self.values[2] == 0.0):
					self.w_history.append(QtCore.QString(str(self.stop_time)))
					self.stop_time = 0
			elif (self.previous_values[2] <= self.values[2]):
				self.stop_time = 0
				
			
			#EMIT values to be shown on the online interface after computing them
			print "******************"
			for w in self.w_history:
				print w
			print "******************"
			time.sleep(1)
			self.emit(QtCore.SIGNAL("onlineUpdate(QStringList)"),self.w_history) #custom signal
			#despues de esto no se ejecuta nada
#TODO: un hilo que actualice los valores de manera automatica siempre que
#haya valores nuevos para mostrar.

#~ if __name__ == "__main__":
	#~ import sys
	#~ app = QtGui.QApplication(sys.argv)
	#~ online = OnlineDialog()
	#~ online.exec_()
	#~ sys.exit(app.exec_())
