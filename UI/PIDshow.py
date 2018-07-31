# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PIDshow.ui'
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
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 301, 226))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonStart = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonStart.sizePolicy().hasHeightForWidth())
        self.pushButtonStart.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonStart.setFont(font)
        self.pushButtonStart.setObjectName(_fromUtf8("pushButtonStart"))
        self.horizontalLayout.addWidget(self.pushButtonStart)
        self.pushButtonBack = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonBack.sizePolicy().hasHeightForWidth())
        self.pushButtonBack.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(14)
        self.pushButtonBack.setFont(font)
        self.pushButtonBack.setObjectName(_fromUtf8("pushButtonBack"))
        self.horizontalLayout.addWidget(self.pushButtonBack)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelPid = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPid.sizePolicy().hasHeightForWidth())
        self.labelPid.setSizePolicy(sizePolicy)
        self.labelPid.setMinimumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Piboto"))
        font.setPointSize(26)
        self.labelPid.setFont(font)
        self.labelPid.setObjectName(_fromUtf8("labelPid"))
        self.gridLayout.addWidget(self.labelPid, 0, 0, 1, 2)
        self.labelValue = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelValue.sizePolicy().hasHeightForWidth())
        self.labelValue.setSizePolicy(sizePolicy)
        self.labelValue.setMinimumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Piboto"))
        font.setPointSize(26)
        self.labelValue.setFont(font)
        self.labelValue.setObjectName(_fromUtf8("labelValue"))
        self.gridLayout.addWidget(self.labelValue, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButtonStart.setText(_translate("Dialog", "Online", None))
        self.pushButtonBack.setText(_translate("Dialog", "Atrás", None))
        self.labelPid.setText(_translate("Dialog", "PID", None))
        self.labelValue.setText(_translate("Dialog", "VALOR", None))

