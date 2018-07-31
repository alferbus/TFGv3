# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pidselect.ui'
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
        Dialog.setMinimumSize(QtCore.QSize(320, 240))
        self.gridLayoutWidget = QtGui.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 303, 221))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonPreviousPID = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonPreviousPID.sizePolicy().hasHeightForWidth())
        self.pushButtonPreviousPID.setSizePolicy(sizePolicy)
        self.pushButtonPreviousPID.setMinimumSize(QtCore.QSize(75, 74))
        font = QtGui.QFont()
        font.setPointSize(41)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonPreviousPID.setFont(font)
        self.pushButtonPreviousPID.setObjectName(_fromUtf8("pushButtonPreviousPID"))
        self.horizontalLayout.addWidget(self.pushButtonPreviousPID)
        self.labelPIDnum = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.labelPIDnum.setFont(font)
        self.labelPIDnum.setObjectName(_fromUtf8("labelPIDnum"))
        self.horizontalLayout.addWidget(self.labelPIDnum)
        self.pushButtonNextPID = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonNextPID.sizePolicy().hasHeightForWidth())
        self.pushButtonNextPID.setSizePolicy(sizePolicy)
        self.pushButtonNextPID.setMinimumSize(QtCore.QSize(75, 74))
        font = QtGui.QFont()
        font.setPointSize(41)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButtonNextPID.setFont(font)
        self.pushButtonNextPID.setObjectName(_fromUtf8("pushButtonNextPID"))
        self.horizontalLayout.addWidget(self.pushButtonNextPID)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.labelPIDname = QtGui.QLabel(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPIDname.sizePolicy().hasHeightForWidth())
        self.labelPIDname.setSizePolicy(sizePolicy)
        self.labelPIDname.setMinimumSize(QtCore.QSize(291, 66))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelPIDname.setFont(font)
        self.labelPIDname.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPIDname.setWordWrap(True)
        self.labelPIDname.setObjectName(_fromUtf8("labelPIDname"))
        self.horizontalLayout_3.addWidget(self.labelPIDname)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButtonBack = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonBack.sizePolicy().hasHeightForWidth())
        self.pushButtonBack.setSizePolicy(sizePolicy)
        self.pushButtonBack.setMinimumSize(QtCore.QSize(146, 59))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(14)
        self.pushButtonBack.setFont(font)
        self.pushButtonBack.setObjectName(_fromUtf8("pushButtonBack"))
        self.horizontalLayout_2.addWidget(self.pushButtonBack)
        self.pushButtonOK = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonOK.sizePolicy().hasHeightForWidth())
        self.pushButtonOK.setSizePolicy(sizePolicy)
        self.pushButtonOK.setMinimumSize(QtCore.QSize(145, 59))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(14)
        self.pushButtonOK.setFont(font)
        self.pushButtonOK.setObjectName(_fromUtf8("pushButtonOK"))
        self.horizontalLayout_2.addWidget(self.pushButtonOK)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButtonPreviousPID.setText(_translate("Dialog", "-", None))
        self.labelPIDnum.setText(_translate("Dialog", "1234", None))
        self.pushButtonNextPID.setText(_translate("Dialog", "+", None))
        self.labelPIDname.setText(_translate("Dialog", "SELECCIONE_UN_PID_PARA_VER", None))
        self.pushButtonBack.setText(_translate("Dialog", "Atrás", None))
        self.pushButtonOK.setText(_translate("Dialog", "Aceptar", None))

