# -*- coding: utf-8 -*-
import os,time,obd #provides several tool functions
from PyQt4 import QtCore, QtGui #provides Qt application libraries
from UI import mainmenu #provides class UI template
import ConfigParser #provides scope to parsing functions

class MainMenuDialog(QtGui.QDialog):
	def __init__(self,obd_path,user_data,user_index, car_index,parent=None):
		QtGui.QWidget.__init__(self, parent)
		
		"""UI SETUP"""
		self.ui = mainmenu.Ui_Dialog() # this brings up the GUI built with QtDesigner
		self.ui.setupUi(self) #calls UI setup function
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint) # removes the window frame
		self.setAttribute(QtCore.Qt.WA_DeleteOnClose,True) # delete dialog on close
		
		#USER DATA
		self.data	= user_data
		self.uindex = user_index
		self.cindex = car_index
		
		#OBD PATH
		self.obd_path = obd_path
		
		"""SIGNAL-SLOTS"""
		#-------------------------- NEW SESSION ------------------------
		self.connect(
			self.ui.pushButtonNewSession, QtCore.SIGNAL('clicked()'),
			self.new_session)
		#-------------------------- CONF SESSION -----------------------
		self.connect(
			self.ui.pushButtonConfSession, QtCore.SIGNAL('clicked()'),
			self.conf_session)
		#--------------------------- SCAN PIDS -------------------------
		self.connect(
			self.ui.pushButtonPidScan, QtCore.SIGNAL('clicked()'),
			self.pid_scan)
		#------------------------------ QUIT ---------------------------
		self.connect(
			self.ui.pushButtonQuit, QtCore.SIGNAL('clicked()'),
			self.quitapp)

	#--------------------------- SLOTS DEFINITION ----------------------
	def new_session(self):
		"""With current username and car, start a recording session by
		proceeding to the PID Selection Dialog. """
		from PidSelectDialog import PidSelectDialog 
		selectPid = PidSelectDialog(self.obd_path,self.data,self.uindex,self.cindex)
		self.close()
		selectPid.exec_()
		
	def conf_session(self):
		"""This can be selected by the user to select both a different 
		user and a different car. It does so by going back to the Login Dialog. """
		from LoginDialog import LoginDialog
		login = LoginDialog(self.obd_path,self.data)
		self.close()
		login.exec_()
		
	def pid_scan(self): 
		"""This option MUST BE selected for the first time a new car is added
		to the pid_list.cfg configuration file. Using the obd library's
		current PID database a list of all supported PID is requested 
		and (over)written to the corresponding section in the pid_list.cfg
		configuration file."""
		self.data.pid_list[self.cindex].clear() #old PID values are cleared
		connection = obd.OBD(self.obd_path) 	#new obd connection to query new car.
		#---------------------------------------------------------------
		config = ConfigParser.SafeConfigParser()#reads pid_list.cfg
		config.read('data/pid_list.cfg')
		car = u'car' + unicode(self.cindex + 1)
		#---------------------------------------------------------------
		for c in connection.supported_commands: #loops through supported command list
			mp = str(c)
			mode_pid = mp[0:4] #stores pid number
			self.data.pid_list[self.cindex][mode_pid]=c.name #stores pid name
			#-----------------------------------------------------------
			config.set(car, unicode(mode_pid), unicode(c.name)) #adds new pid to list
		#---------------------------------------------------------------	
		with open('data/pid_list.cfg', 'r+') as configfile:
			config.write(configfile) #writes all new pids to corresponding
									#config file
			
	def quitapp(self):
		raise SystemExit #quits software by raising a termination exception
