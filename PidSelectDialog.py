# -*- coding: utf-8 -*-
import os,time,obd #provides several tool functions
from PyQt4 import QtCore, QtGui #provides Qt application libraries
from UI import pidselect #provides class UI template

class PidSelectDialog(QtGui.QDialog):
	def __init__(self,obd_path,user_data,user_index,car_index,parent=None):
		QtGui.QWidget.__init__(self, parent)
		
		"""UI SETUP"""
		self.ui = pidselect.Ui_Dialog() # this brings up the GUI built with QtDesigner
		self.ui.setupUi(self) #calls UI setup function
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint) # removes the window frame
		self.setAttribute(QtCore.Qt.WA_DeleteOnClose,True) # deletes dialog on close
		
		#USER DATA
		self.data = user_data
		self.uindex = user_index
		self.cindex = car_index
		
		#OBD PATH
		self.obd_path = obd_path
		
		#PID LIST
		"""This sentence stores a list of all the available PIDs to
		be shown sorted by name. In order to do that, current car index
		is needed to copy all PIDs corresponding to the current car selected
		by the user."""
		self.__PIDS = sorted(
			self.data.pid_list[self.cindex],
			key=self.data.pid_list[self.cindex].get) 
		
		#CURRENT PID
		self.__i = 0 #current index, to track which PID is being shown.
		self.current_pid_number = self.__PIDS[self.__i]
		self.current_pid_name = self.data.pid_list[self.cindex][self.__PIDS[self.__i]]
		"""self.__PIDS contains only the PID numbers. To get PID names, 
		PID numbers are also required: self.__PIDS[self.__i] thus stands
		for 'current pid number'.
		Full syntax would be:
		self.data.pid_list[self.cindex]['pid_number']
				|				|			|
		from pid_list  from current vehicle current pid number.
		Separate variable names 'self.current_pid_number' and 'self.current_pid_name'
		are used for improved readability"""
		
		#SHOW CURRENT PID
		self.__show_current_pid() #shows first element of the pid 'wheel'
		                          #of elements.
		
		"""SHOW UI"""
		#------------------------- NEXT PID ----------------------------
		self.connect(
			self.ui.pushButtonNextPID, QtCore.SIGNAL('clicked()'),
			self.next_pid)
		#----------------------- PREVIOUS PID --------------------------
		self.connect(
			self.ui.pushButtonPreviousPID, QtCore.SIGNAL('clicked()'),
			self.previous_pid)
		#--------------------------- BACK ------------------------------
		self.connect(
			self.ui.pushButtonBack, QtCore.SIGNAL('clicked()'),
			self.back_to_main_menu)
		#---------------------------- OK -------------------------------
		self.connect(
			self.ui.pushButtonOK, QtCore.SIGNAL('pressed()'),
			self.OK_pressed)
		self.connect(
			self.ui.pushButtonOK, QtCore.SIGNAL('released()'),
			self.OK_released)
	
	def __show_current_pid(self):
		"""This method is in charge of showing in the Dialog's label
		the PID (both name and numer) corresponding to the current number
		index. It is a working function which only reads the index to 
		show it. It DOESN'T move the index number self.__i"""
		self.current_pid_number = self.__PIDS[self.__i]
		self.current_pid_name = self.data.pid_list[self.cindex][self.__PIDS[self.__i]]
		"""self.__PIDS contains only the PID numbers. To get PID names, 
		PID numbers are also required: self.__PIDS[self.__i] thus stands
		for 'current pid number'.
		Full syntax would be:
		self.data.pid_list[self.cindex]['pid_number']
				|				|			|
		from pid_list  from current vehicle current pid number.
		Separate variable names 'self.current_pid_number' and 'self.current_pid_name'
		are used for improved readability"""
		self.ui.labelPIDname.clear()
		self.ui.labelPIDnum.setText(self.current_pid_number)
		self.ui.labelPIDname.setText(self.current_pid_name)
		
	#--------------------------- SLOTS DEFINITION ----------------------
	def next_pid(self):
		"""Increments index number by 1 unit, making sure it is not out 
		of range, that is, when end is reached it goes back to the FIRST
		element."""
		self.__i+=1                      #increment index
		if self.__i < len(self.__PIDS):  #if index is NOT out of range				
			self.__show_current_pid()    #proceed to show current pid	
		else:                            #if index IS out of range
			self.__i=0                   #go back to the first element
			self.__show_current_pid()	 #proceed to show the first element
			
	def previous_pid(self):
		"""Decrements index number by 1 unit, making sure it is not out 
		of range, that is, when end is reached it goes back to the LAST
		element."""
		self.__i-=1                      #decrement index
		if self.__i >= 0:                #if index is NOT out of range
			self.__show_current_pid()    #proceed to show current pid	
		else:                            #if index IS out of range
			self.__i=(len(self.__PIDS)-1)#go back to the last element
			self.__show_current_pid()	 #proceed to show the last element
			
	def back_to_main_menu(self):
		"""Simply allows the user to return to the Main Menu Dialog"""
		#NOTE: class imported here to prevent scope name problems
		from MainMenuDialog import MainMenuDialog
		mainm = MainMenuDialog(self.obd_path,self.data,self.uindex,self.cindex)
		self.close()
		mainm.exec_
		
	def OK_pressed(self):
		"""Tells the user to wait until next Dialog is loaded when OK
		push button is pressed."""
		self.ui.pushButtonOK.setFlat(True)
		self.ui.pushButtonOK.setText("Espere...")
		
	def OK_released(self):
		"""Loads the Pid Show Dialog by instantiating and passing all the
		required arguments"""
		#NOTE: class imported here to prevent scope name problems
		from PidShowDialog import PidShowDialog
		pid_show =  PidShowDialog(
			self.obd_path,self.data,self.uindex,self.cindex,self.current_pid_name)
		self.close()
		pid_show.exec_()
