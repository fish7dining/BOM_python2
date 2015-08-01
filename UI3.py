# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog2.ui'
#
# Created: Sat Aug  1 19:05:17 2015
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_Dialog2(object):
    def setupUi(self, Dialog2):
        Dialog2.setObjectName(_fromUtf8("Dialog2"))
        Dialog2.resize(661, 199)
        self.label = QtGui.QLabel(Dialog2)
        self.label.setGeometry(QtCore.QRect(70, 40, 51, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog2)
        self.label_2.setGeometry(QtCore.QRect(220, 40, 31, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog2)
        self.label_3.setGeometry(QtCore.QRect(340, 40, 141, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog2)
        self.label_4.setGeometry(QtCore.QRect(510, 40, 101, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton = QtGui.QPushButton(Dialog2)
        self.pushButton.setGeometry(QtCore.QRect(190, 140, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog2)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 140, 99, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.comboBox = QtGui.QComboBox(Dialog2)
        self.comboBox.setGeometry(QtCore.QRect(20, 70, 131, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox_2 = QtGui.QComboBox(Dialog2)
        self.comboBox_2.setGeometry(QtCore.QRect(170, 70, 131, 27))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_3 = QtGui.QComboBox(Dialog2)
        self.comboBox_3.setGeometry(QtCore.QRect(500, 70, 131, 27))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.lineEdit = QtGui.QLineEdit(Dialog2)
        self.lineEdit.setGeometry(QtCore.QRect(360, 70, 71, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(Dialog2)
        QtCore.QMetaObject.connectSlotsByName(Dialog2)

    def retranslateUi(self, Dialog2):
        Dialog2.setWindowTitle(_translate("Dialog2", "Dialog", None))
        self.label.setText(_translate("Dialog2", "Father", None))
        self.label_2.setText(_translate("Dialog2", "Son", None))
        self.label_3.setText(_translate("Dialog2", "Ratio ( Father : Son )", None))
        self.label_4.setText(_translate("Dialog2", "Product Code", None))
        self.pushButton.setText(_translate("Dialog2", "Cancel", None))
        self.pushButton_2.setText(_translate("Dialog2", "Yes", None))

