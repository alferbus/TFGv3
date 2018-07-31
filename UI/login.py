# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
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
        Dialog.resize(335, 240)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 5, 0, 1, 1)
        self.comboBoxUser = QtGui.QComboBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxUser.sizePolicy().hasHeightForWidth())
        self.comboBoxUser.setSizePolicy(sizePolicy)
        self.comboBoxUser.setMinimumSize(QtCore.QSize(299, 45))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.comboBoxUser.setFont(font)
        self.comboBoxUser.setObjectName(_fromUtf8("comboBoxUser"))
        self.gridLayout.addWidget(self.comboBoxUser, 1, 0, 1, 1)
        self.pushButtonOK = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonOK.sizePolicy().hasHeightForWidth())
        self.pushButtonOK.setSizePolicy(sizePolicy)
        self.pushButtonOK.setMinimumSize(QtCore.QSize(299, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(14)
        self.pushButtonOK.setFont(font)
        self.pushButtonOK.setObjectName(_fromUtf8("pushButtonOK"))
        self.gridLayout.addWidget(self.pushButtonOK, 6, 0, 1, 1)
        self.labelUser = QtGui.QLabel(Dialog)
        self.labelUser.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelUser.sizePolicy().hasHeightForWidth())
        self.labelUser.setSizePolicy(sizePolicy)
        self.labelUser.setMinimumSize(QtCore.QSize(299, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(16)
        self.labelUser.setFont(font)
        self.labelUser.setObjectName(_fromUtf8("labelUser"))
        self.gridLayout.addWidget(self.labelUser, 0, 0, 1, 1)
        self.labelVehicle = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelVehicle.sizePolicy().hasHeightForWidth())
        self.labelVehicle.setSizePolicy(sizePolicy)
        self.labelVehicle.setMinimumSize(QtCore.QSize(299, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(16)
        self.labelVehicle.setFont(font)
        self.labelVehicle.setObjectName(_fromUtf8("labelVehicle"))
        self.gridLayout.addWidget(self.labelVehicle, 2, 0, 1, 1)
        self.comboBoxVehicle = QtGui.QComboBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxVehicle.sizePolicy().hasHeightForWidth())
        self.comboBoxVehicle.setSizePolicy(sizePolicy)
        self.comboBoxVehicle.setMinimumSize(QtCore.QSize(299, 45))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(16)
        self.comboBoxVehicle.setFont(font)
        self.comboBoxVehicle.setObjectName(_fromUtf8("comboBoxVehicle"))
        self.gridLayout.addWidget(self.comboBoxVehicle, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.comboBoxUser, self.comboBoxVehicle)
        Dialog.setTabOrder(self.comboBoxVehicle, self.pushButtonOK)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButtonOK.setText(_translate("Dialog", "Aceptar", None))
        self.labelUser.setText(_translate("Dialog", "Usuario:", None))
        self.labelVehicle.setText(_translate("Dialog", "Vehículo:", None))

