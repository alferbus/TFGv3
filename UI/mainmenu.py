# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainmenu.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(320, 240)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButtonNewSession = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonNewSession.sizePolicy().hasHeightForWidth())
        self.pushButtonNewSession.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButtonNewSession.setFont(font)
        self.pushButtonNewSession.setObjectName(_fromUtf8("pushButtonNewSession"))
        self.gridLayout.addWidget(self.pushButtonNewSession, 0, 0, 1, 1)
        self.pushButtonConfSession = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonConfSession.sizePolicy().hasHeightForWidth())
        self.pushButtonConfSession.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButtonConfSession.setFont(font)
        self.pushButtonConfSession.setObjectName(_fromUtf8("pushButtonConfSession"))
        self.gridLayout.addWidget(self.pushButtonConfSession, 1, 0, 1, 1)
        self.pushButtonPidScan = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonPidScan.sizePolicy().hasHeightForWidth())
        self.pushButtonPidScan.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButtonPidScan.setFont(font)
        self.pushButtonPidScan.setObjectName(_fromUtf8("pushButtonPidScan"))
        self.gridLayout.addWidget(self.pushButtonPidScan, 2, 0, 1, 1)
        self.pushButtonQuit = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonQuit.sizePolicy().hasHeightForWidth())
        self.pushButtonQuit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButtonQuit.setFont(font)
        self.pushButtonQuit.setObjectName(_fromUtf8("pushButtonQuit"))
        self.gridLayout.addWidget(self.pushButtonQuit, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButtonNewSession.setText(_translate("Dialog", "Nueva sesión", None))
        self.pushButtonConfSession.setText(_translate("Dialog", "Configurar sesión", None))
        self.pushButtonPidScan.setText(_translate("Dialog", "Escanear PIDs", None))
        self.pushButtonQuit.setText(_translate("Dialog", "SALIR", None))

