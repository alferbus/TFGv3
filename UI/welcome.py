# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
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
        Dialog.setMinimumSize(QtCore.QSize(320, 240))
        Dialog.setSizeGripEnabled(False)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pushButtonUserList = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonUserList.sizePolicy().hasHeightForWidth())
        self.pushButtonUserList.setSizePolicy(sizePolicy)
        self.pushButtonUserList.setMinimumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonUserList.setFont(font)
        self.pushButtonUserList.setObjectName(_fromUtf8("pushButtonUserList"))
        self.verticalLayout_2.addWidget(self.pushButtonUserList)
        self.pushButtonQuit = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonQuit.sizePolicy().hasHeightForWidth())
        self.pushButtonQuit.setSizePolicy(sizePolicy)
        self.pushButtonQuit.setMinimumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonQuit.setFont(font)
        self.pushButtonQuit.setObjectName(_fromUtf8("pushButtonQuit"))
        self.verticalLayout_2.addWidget(self.pushButtonQuit)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.labelWelcome = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelWelcome.sizePolicy().hasHeightForWidth())
        self.labelWelcome.setSizePolicy(sizePolicy)
        self.labelWelcome.setMinimumSize(QtCore.QSize(300, 106))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(16)
        self.labelWelcome.setFont(font)
        self.labelWelcome.setObjectName(_fromUtf8("labelWelcome"))
        self.horizontalLayout_2.addWidget(self.labelWelcome)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButtonUserList.setText(_translate("Dialog", "Lista de usuarios/as", None))
        self.pushButtonQuit.setText(_translate("Dialog", "Salir", None))
        self.labelWelcome.setText(_translate("Dialog", "Bienvenido/a:\n"
"Por favor, seleccione una\n"
"opción.", None))

