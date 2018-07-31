# -*- coding: utf-8 -*-
# required imports
import sys 
from PyQt4 import QtCore, QtGui
from WelcomeDialog import WelcomeDialog

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	try:
		obd_path = sys.argv[1]
	except IndexError as ie:
		mb = QtGui.QMessageBox (
			u'Error',u'Introduzca ruta del disp. OBD',
			QtGui.QMessageBox.Critical,QtGui.QMessageBox.Ok,0,0)
		mb.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		mb.setAttribute(QtCore.Qt.WA_DeleteOnClose,True) # delete dialog on close
		mb.exec_() #prevent focus loss
		raise SystemExit #No gps device found -- QUIT
	#print('ARGS: %s' %sys.argv[1])
	welcome = WelcomeDialog(obd_path)
	welcome.exec_() #prevents focus loss
	sys.exit(app.exec_())
