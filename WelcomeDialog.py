# -*- coding: utf-8 -*-

import sys,os,time
from PyQt4 import QtCore, QtGui
from UI import welcome
from data import cfgparser
from gps3 import agps3

class UserData(object):
	def __init__(self):
		"""This class acts as a wrapper of all data retrieved from 
		config. files. These .cfg files are available to the user inside
		the 'data' folder and can be edited in an easy-to-read, 
		plain-text format"""
		self.user_list = cfgparser.get_users() 	#parses user_list.cfg
		self.car_list = cfgparser.get_cars() 	#parses car_list.cfg
		self.pid_list = cfgparser.get_pids()	#parser pid_list.cfg
		
class WelcomeDialog(QtGui.QDialog):
	def __init__(self,obd_path,parent=None): #Parent-child class filiation is solved automatically
		QtGui.QWidget.__init__(self, parent)
		""" This brings up the login dialog interface"""
		#------------------------ UI SETUP -----------------------------
		self.ui = welcome.Ui_Dialog() #this brings up the GUI built with QtDesigner
		self.ui.setupUi(self) #calls UI setup function
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint) #removes the window frame
		self.setAttribute(QtCore.Qt.WA_DeleteOnClose,True) #deletes dialog object from memory on close
		#------------------------ DATA READ  ---------------------------
		self.data = UserData() #provides wrapper for easy data access
		self.obd_path = obd_path
		#---------------------- SIGNAL - SLOTS -------------------------
		"""Each QDialog child class features a connect method inherited
		from its parent class. It is used as a high level interface for 
		event handling. Each time the user interacts with the app 
		(that is, he or she presses/releases a button, clicks on
		anything, etc.) a 'signal' is sent, acting as a flag.
		Then, the 'slot' (associated method) is triggered"""
		"""A 'slot' can either be predefined by Qt or user-made"""
		self.connect(
			self.ui.pushButtonUserList, QtCore.SIGNAL('pressed()'),
			self.change_button) 		#user-made slot
		self.connect(
			self.ui.pushButtonUserList, QtCore.SIGNAL('released()'),
			self.check_GPS_show_users)	#user-made slot
		self.connect(
			self.ui.pushButtonQuit, QtCore.SIGNAL("clicked()"), 
			self.quitapp)				#user-made slot
	#--------------------------- SLOTS DEFINITION ----------------------
	def change_button(self):
		#Sets the button flat to tell the user to wait for GPS
		self.ui.pushButtonUserList.setFlat(True)
		self.ui.pushButtonUserList.setText(u"Espere al FIX del GPS...")
	
	def quitapp(self):
		raise SystemExit #Raises SystemExit exception to quit the app.
	
	def check_GPS_show_users(self):
		"""GPS FIX"""
		#Sets flat 'show user list button' so that the user knows the 
		#software is still working.""
		self.ui.pushButtonUserList.setFlat(True)
		self.ui.pushButtonUserList.setText(u"Espere al FIX del GPS...")
		#R-pi GPSD needs to be disabled as well:
		"""Raspbian default install already features a gpsd daemon of 
		its own. We will be calling it on demand so it needs to be
		disabled due to compatibility issues, as both instances cannot be
		running at once."""
		os.system('sudo systemctl stop gpsd.socket')
		os.system('sudo systemctl disable gpsd.socket')
		""" Communication with the GPS device takes place using the agps3
		library, available through pip. This library acts as an interface
		to parse the raw data provided by the gpsd daemon. In order to
		get the data a GPS fix (i.e. a working satellite link) is
		required. """
		try:
			gpsd_socket = agps3.GPSDSocket() #Opens a 'socket' form which
											 #can be polled
			data_stream = agps3.DataStream() #Opens a new data stream
											 #inside the socket
			gpsd_socket.connect() #Links to the socket.
			gpsd_socket.watch()   #Watches the socket for changes.
			#Tries to grab an object from the data stream.
			#If no new objects are found inside the data stream, an 
			#exception is issued warning the user to check the gps link.
			#If there's a working link but no fix, then the gps device
			#will be repeatedly polled until success.
			#Meanwhile, the user is instructed to wait patiently.
			for new_data in gpsd_socket:
				if new_data:
					data_stream.unpack(new_data)
				if data_stream.lat != 'n/a':
					break
		except (OSError, IOError):
			mb = QtGui.QMessageBox (
			u'Advertencia',u'Compruebe la conexión del GPS',
			QtGui.QMessageBox.Warning,QtGui.QMessageBox.Ok,0,0)
			mb.setWindowFlags(QtCore.Qt.FramelessWindowHint)
			mb.setAttribute(QtCore.Qt.WA_DeleteOnClose,True) # delete dialog on close
			mb.exec_() #prevent focus loss
			raise SystemExit #No gps device found -- QUIT
			
		#Now a login dialog object is created with all the 
		#collected user data as an argument
		from LoginDialog import LoginDialog
		login = LoginDialog(self.obd_path,self.data)
		self.close() #closes login dialog
		login.exec_() #keeps focus on loginion dialog
