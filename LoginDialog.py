# -*- coding: utf-8 -*-
import os,time,obd
from PyQt4 import QtCore, QtGui
from UI import login
from gps3 import agps3

class LoginDialog(QtGui.QDialog):
	def __init__(self,obd_path,user_data, parent=None):
		QtGui.QWidget.__init__(self, parent)
		""" This brings up the user loginion dialog"""
		
		"""UI SETUP"""
		self.ui = login.Ui_Dialog() #this brings up the GUI built with QtDesigner
		self.ui.setupUi(self) #calls UI setup function
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint) #removes the window frame
		self.setAttribute(QtCore.Qt.WA_DeleteOnClose,True) #deletes dialog object from memory on close
		
		#USER DATA
		self.data = user_data 
		self.obd_path = obd_path
		
		#COMBO BOX SETUP
		#Reads the previously parsed user data and displays it nicely on
		#combo-boxes so that the user can easily choose both a username
		#and a car.
		for one_user in self.data.user_list: #show registered users
			self.ui.comboBoxUser.addItem(one_user['name'])
		for one_car in self.data.car_list: #show added cars
			self.ui.comboBoxVehicle.addItem(
			one_car['maker']+' '+one_car['model'])
		
		"""SIGNAL-SLOTS"""
		self.connect(
			self.ui.pushButtonOK, QtCore.SIGNAL('pressed()'),
			self.OK)
		self.connect(
			self.ui.pushButtonOK, QtCore.SIGNAL('released()'),
			self.check_obd)

	#--------------------------- SLOTS DEFINITION ----------------------	
	def OK(self):
		self.ui.pushButtonOK.setFlat(True)
		self.ui.pushButtonOK.setText(u"Comprobando conexión OBD...")
		#Ejecutar ventana de selección de PID
	"""Python's obd library (available from pip) is used to retrieve OBD
	data from the car. A new obd object is created which automatically
	sets up the link. If successful, the protocol name is shown. If not,
	an error mesage is shown. """	
	def check_obd(self):
		connection = obd.OBD(self.obd_path)
		protocol_name = connection.protocol_name()
		if connection.is_connected():
			mb = QtGui.QMessageBox (
			u'¡Éxito!',unicode(connection.status())+
			u"\nmediante "+unicode(connection.protocol_name()),
			QtGui.QMessageBox.Information,QtGui.QMessageBox.Ok,0,0)
			mb.setWindowFlags(QtCore.Qt.FramelessWindowHint)
			mb.setAttribute(QtCore.Qt.WA_DeleteOnClose,True) # delete dialog on close
			mb.exec_() #prevent focus loss
		else:
			mb = QtGui.QMessageBox (
			u'Error',u'Error de conexión.\nRevise adaptador.',
			QtGui.QMessageBox.Critical,QtGui.QMessageBox.Ok,0,0)
			mb.setWindowFlags(QtCore.Qt.FramelessWindowHint)
			mb.setAttribute(QtCore.Qt.WA_DeleteOnClose,True) # delete dialog on close
			mb.exec_() #prevent focus loss
		
		connection.close()
		self.ui.pushButtonOK.setFlat(False)
		self.ui.pushButtonOK.setText(unicode(protocol_name)+u'\nContinuar')
		
		from MainMenuDialog import MainMenuDialog
		#Get current user and current vehicle indexes
		#They were input in an ordered fashion so we can retrieve them
		#the same way
		user_index = self.ui.comboBoxUser.currentIndex()
		car_index  = self.ui.comboBoxVehicle.currentIndex()
		
		mainm = MainMenuDialog(self.obd_path,self.data,user_index, car_index)
		self.close() #also deletes LoginDialog object safely
		mainm.exec_()
