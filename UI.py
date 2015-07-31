# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Jul 31 20:17:10 2015
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1004, 524)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.tableView = QtGui.QTableView(self.centralWidget)
        self.tableView.setGeometry(QtCore.QRect(20, 20, 351, 381))
        self.tableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 410, 101, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 410, 101, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.tableView_2 = QtGui.QTableView(self.centralWidget)
        self.tableView_2.setGeometry(QtCore.QRect(390, 20, 391, 381))
        self.tableView_2.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableView_2.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableView_2.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableView_2.setObjectName(_fromUtf8("tableView_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 410, 101, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(500, 410, 101, 31))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_5.setGeometry(QtCore.QRect(810, 100, 161, 51))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_6.setGeometry(QtCore.QRect(810, 170, 161, 51))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_7.setGeometry(QtCore.QRect(810, 240, 161, 51))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_9 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_9.setGeometry(QtCore.QRect(810, 380, 161, 51))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_8 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_8.setGeometry(QtCore.QRect(810, 310, 161, 51))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.lineEdit = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(810, 50, 161, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(810, 30, 161, 17))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1004, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "material_add", None))
        self.pushButton_2.setText(_translate("MainWindow", "material_del", None))
        self.pushButton_3.setText(_translate("MainWindow", "relation_add", None))
        self.pushButton_4.setText(_translate("MainWindow", "relation_del", None))
        self.pushButton_5.setText(_translate("MainWindow", "single query", None))
        self.pushButton_6.setText(_translate("MainWindow", "multi query", None))
        self.pushButton_7.setText(_translate("MainWindow", "single reverse query", None))
        self.pushButton_9.setText(_translate("MainWindow", "end product query", None))
        self.pushButton_8.setText(_translate("MainWindow", "multi reverse query", None))
        self.label.setText(_translate("MainWindow", "Input material code : ", None))

