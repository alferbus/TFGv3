# -*- coding: utf-8 -*-
import os,time,obd #provides several tool functions
from PyQt4 import QtCore, QtGui #provides Qt application libraries
from UI import mainmenu #provides class UI template
import ConfigParser


class MainMenuDialog(QtGui.QDialog):
	def __init__(self,obd_path,user_data,user_index, car_index,parent=None):
		QtGui.QWidget.__init__(self, parent)
		
		"""UI SETUP"""
		self.ui = mainmenu.Ui_Dialog() # this brings up the GUI built with QtDesigner
		self.ui.setupUi(self)
		self.setWindowFlags(
			QtCore.Qt.FramelessWindowHint) # remove the window frame
			# ~ | QtCore.Qt.WindowStaysOnTopHint) # keep the focus
		self.setAttribute(QtCore.Qt.WA_DeleteOnClose,True) # delete dialog on close
		
		#USER DATA
		self.data = user_data
		self.uindex = user_index
		self.cindex = car_index
		
		#OBD PATH
		self.obd_path = obd_path
		"""SHOW UI"""
		
		#-------------------------- NEW SESSION -----------------------
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
		
	def new_session(self):
		from PidSelectDialog import PidSelectDialog 
		#self.pid_scan() # to make sure all PIDS are stored
		selectPid = PidSelectDialog(self.obd_path,self.data,self.uindex,self.cindex)
		self.close()
		selectPid.exec_()
	def conf_session(self):
		from LoginDialog import LoginDialog
		login = LoginDialog(self.obd_path,self.data)
		self.close()
		login.exec_()
		
	def pid_scan(self):
		self.data.pid_list[self.cindex].clear() #to replace old PID values
		print self.data.pid_list[self.cindex]
		connection = obd.OBD(self.obd_path)
		#---------------------------------------------------------------
		config = ConfigParser.SafeConfigParser()
		config.read('data/pid_list.cfg')
		car = u'car' + unicode(self.cindex + 1)
		#---------------------------------------------------------------
		for c in connection.supported_commands:
			mp = str(c)
			mode_pid = mp[0:4]
			self.data.pid_list[self.cindex][mode_pid]=c.name
			#~ mode_pid = u'0'+unicode(c.mode)+unicode(c.pid)
			#~ self.data.pid_list[self.cindex][mode_pid]=c.name
			#-----------------------------------------------------------
			config.set(car, unicode(mode_pid), unicode(c.name))
		#---------------------------------------------------------------	
		print self.data.pid_list[self.cindex]
		
		with open('data/pid_list.cfg', 'r+') as configfile:
			config.write(configfile)
			
	def quitapp(self):
		raise SystemExit
	
		
	#~ def check_obd_and_pass(self):
		#~ connection = obd.OBD('/dev/pts/4') #TODO: hacerlo para bluetooth
										   #~ #TODO: posible pantalla de selección de puerto??
		#~ ptrcl = connection.protocol_name()
		#~ if connection.is_connected():
			#~ mb = QtGui.QMessageBox (
			#~ u'¡Éxito!',unicode(connection.status())+
			#~ u"\nmediante "+unicode(connection.protocol_name()),
			#~ QtGui.QMessageBox.Information,QtGui.QMessageBox.Ok,0,0)
			#~ mb.setWindowFlags(QtCore.Qt.FramelessWindowHint)
			#~ mb.setAttribute(QtCore.Qt.WA_DeleteOnClose,True) # delete dialog on close
			#~ mb.exec_() #prevent focus loss
		#~ else:
			#~ mb = QtGui.QMessageBox (
			#~ u'Error',u'Error de conexión.\nRevise adaptador.',
			#~ QtGui.QMessageBox.Critical,QtGui.QMessageBox.Ok,0,0)
			#~ mb.setWindowFlags(QtCore.Qt.FramelessWindowHint)
			#~ mb.setAttribute(QtCore.Qt.WA_DeleteOnClose,True) # delete dialog on close
			#~ mb.exec_() #prevent focus loss
		
		#~ connection.close()
		#~ self.ui.pushButtonOK.setFlat(False)
		#~ self.ui.pushButtonOK.setText(unicode(ptrcl)+u'\nContinuar')
		

		#~ #raise SystemExit #QUIT

#~ if __name__ == "__main__":
	#~ import sys
	#~ app = QtGui.QApplication(sys.argv)
	#~ mainm = MainMenuDialog()
	#~ mainm.exec_()
	#~ sys.exit(app.exec_())
