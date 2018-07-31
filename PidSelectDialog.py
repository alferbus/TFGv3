# -*- coding: utf-8 -*-
import os,time,obd
from PyQt4 import QtCore, QtGui
from UI import pidselect


#TODO: Wrapper class for user_list, car_list, pid_list. 

class PidSelectDialog(QtGui.QDialog):
	def __init__(self,obd_path,user_data,user_index,car_index,parent=None):
		QtGui.QWidget.__init__(self, parent)
		
		"""UI SETUP"""
		self.ui = pidselect.Ui_Dialog() # this brings up the GUI built with QtDesigner
		self.ui.setupUi(self)
		self.setWindowFlags(
			QtCore.Qt.FramelessWindowHint) # remove the window frame
			# ~ | QtCore.Qt.WindowStaysOnTopHint) # keep the focus
		self.setAttribute(QtCore.Qt.WA_DeleteOnClose,True) # delete dialog on close
		#USER DATA
		self.data = user_data
		self.uindex = user_index
		self.cindex = car_index
		
		self.obd_path = obd_path
		#LOOPING OVER PIDS #TODO: print self.__PIDS para ver qué ha salido
		self.__PIDS = sorted(
			self.data.pid_list[self.cindex],
			key=self.data.pid_list[self.cindex].get) #list of sorted PIDS
		self.__i = 0 #current index, to track which PID is being shown.
		self.current_pid_number = self.__PIDS[self.__i]
		self.current_pid_name = self.data.pid_list[self.cindex][self.__PIDS[self.__i]]
		#SHOW CURRENT PID
		self.__show_current_pid()
		"""SHOW UI"""
		#~ #---------------------- NEXT PID ----------------------------
		self.connect(
			self.ui.pushButtonNextPID, QtCore.SIGNAL('clicked()'),
			self.next_pid)
		#----------------------- PREVIOUS PID --------------------------
		self.connect(
			self.ui.pushButtonPreviousPID, QtCore.SIGNAL('clicked()'),
			self.previous_pid)
		#~ #------------------------ BACK ------------------------------
		self.connect(
			self.ui.pushButtonBack, QtCore.SIGNAL('clicked()'),
			self.back_to_main_menu)
		#~ #------------------------- OK -------------------------------
		self.connect(
			self.ui.pushButtonOK, QtCore.SIGNAL('pressed()'),
			self.OK_pressed)
		self.connect(
			self.ui.pushButtonOK, QtCore.SIGNAL('released()'),
			self.OK_released)
	
	def __show_current_pid(self):
		self.current_pid_number = self.__PIDS[self.__i]
		self.current_pid_name = self.data.pid_list[self.cindex][self.__PIDS[self.__i]]
	
		self.ui.labelPIDname.clear()
		self.ui.labelPIDnum.setText(self.current_pid_number)
		self.ui.labelPIDname.setText(self.current_pid_name)
		
		#~ self.ui.plainTextEditPIDnum.appendPlainText(
			#~ self.__PIDS[self.__i]) #TODO: que no se muestren todos los pIDS Seguidos
		
	def next_pid(self):
		self.__i+=1
		if self.__i < len(self.__PIDS):				
			self.__show_current_pid()		
		else:
			self.__i=0
			self.__show_current_pid()
	def previous_pid(self):
		self.__i-=1
		if self.__i >= 0:				
			self.__show_current_pid()		
		else:
			self.__i=(len(self.__PIDS)-1)
			self.__show_current_pid()
	def back_to_main_menu(self):
		from MainMenuDialog import MainMenuDialog
		mainm = MainMenuDialog(self.obd_path,self.data,self.uindex,self.cindex)
		self.close()
		mainm.exec_()
	def OK_pressed(self):
		self.ui.pushButtonOK.setFlat(True)
		self.ui.pushButtonOK.setText("Espere...")
	def OK_released(self):
		from PidShowDialog import PidShowDialog
		pid_show =  PidShowDialog(
			self.obd_path,self.data,self.uindex,self.cindex,self.current_pid_name)
		self.close()
		pid_show.exec_()
#~ if __name__ == "__main__":
	#~ import sys
	#~ app = QtGui.QApplication(sys.argv)
	#~ login = PidSelectDialog()
	#~ login.exec_()
	#~ sys.exit(app.exec_())
