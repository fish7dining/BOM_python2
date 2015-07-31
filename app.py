#!/usr/bin/env python

import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMessageBox
from PyQt4.QtSql import QSqlDatabase, QSqlTableModel
from UI import Ui_MainWindow
from UI2 import Ui_Dialog
from UI3 import Ui_Dialog2
import sqlite3
import single_query, multi_query, single_reverse_query, multi_reverse_query



class second(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.bye)
        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL("clicked()"), self.add)

    def add(self):
        code = self.ui.textEdit.toPlainText()
        name = self.ui.textEdit_2.toPlainText()
        CX = sqlite3.connect("data.db")
        CU = CX.cursor()
        CU.execute("select * from material where code = '"+str(code)+"'")
        ans = CU.fetchall()
        if len(ans) > 0:
            QMessageBox.warning(self, "Wrong", 'Code Name has already exist!')
        else:
            CU.execute("insert into material values(?,?,?)",(None, str(code), str(name)))
            CX.commit()
            myapp.model.select()
            print 'insert successfully'
            self.close()

    def bye(self):
        self.close()


class third(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog2()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.bye)
        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL("clicked()"), self.add)
        CX = sqlite3.connect("data.db")
        CU = CX.cursor()
        CU.execute("select * from material")
        ans = CU.fetchall()
        self.mp = {}
        for i in ans:
            self.mp[str(i[1])] = i[0]
            self.ui.comboBox.addItem(str(i[1]))
            self.ui.comboBox_2.addItem(str(i[1]))
            self.ui.comboBox_3.addItem(str(i[1]))
    def add(self):
        if self.ui.lineEdit.text() != '':
            fatherID = self.mp[str(self.ui.comboBox.currentText())]
            sonID = self.mp[str(self.ui.comboBox_2.currentText())]
            productCode = str(self.ui.comboBox_3.currentText())
            ratios = int(self.ui.lineEdit.text())
            CX = sqlite3.connect("data.db")
            CU = CX.cursor()
            CU.execute("select * from relation where father = '"+str(fatherID)+ \
                       "' and son = '"+str(sonID)+"' and product_code = '"+productCode+"'")
            ans = CU.fetchall()
            if len(ans)==0:
                CU.execute("insert into relation values(?,?,?,?,?)",(None, fatherID, sonID, ratios, productCode))
                CX.commit()
                print 'insert successfully'
                myapp.model2.select()
                self.close()
            else:
                reply = QMessageBox.warning(self, "TABLE relation", 'Has already existed!')
        else:
            reply = QMessageBox.warning(self, "TABLE relation", 'ratio is empty!')

    def bye(self):
        self.close()



class first(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("/home/valseek/PycharmProjects/bom/data.db")
        if db.open():
            print "Open data.db successfully"
        else:
            print "Could not open data.db"
        self.model = QSqlTableModel(self, db)
        self.model.setTable("material")
        self.model.select()
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setColumnWidth(0, 45)
        self.ui.tableView.setColumnWidth(1, 150)
        self.ui.tableView.setColumnWidth(2, 110)

        self.model2 = QSqlTableModel(self, db)
        self.model2.setTable("relation")
        self.model2.select()
        self.ui.tableView_2.setModel(self.model2)
        self.ui.tableView_2.setColumnWidth(0, 45)
        self.ui.tableView_2.setColumnWidth(1, 55)
        self.ui.tableView_2.setColumnWidth(2, 45)
        self.ui.tableView_2.setColumnWidth(3, 45)
        self.ui.tableView_2.setColumnWidth(4, 150)


        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.addMaterial)
        QtCore.QObject.connect(self.ui.pushButton_3, QtCore.SIGNAL("clicked()"), self.addRelation)
        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL("clicked()"), self.deleteMaterial)
        QtCore.QObject.connect(self.ui.pushButton_4, QtCore.SIGNAL("clicked()"), self.deleteRelation)

        QtCore.QObject.connect(self.ui.pushButton_5, QtCore.SIGNAL("clicked()"), self.singleQuery)
        QtCore.QObject.connect(self.ui.pushButton_6, QtCore.SIGNAL("clicked()"), self.multiQuery)
        QtCore.QObject.connect(self.ui.pushButton_7, QtCore.SIGNAL("clicked()"), self.singleReverseQuery)
        QtCore.QObject.connect(self.ui.pushButton_8, QtCore.SIGNAL("clicked()"), self.multiReverseQuery)
        #QtCore.QObject.connect(self.ui.pushButton_9, QtCore.SIGNAL("clicked()"), self.deleteRelation)


    def singleQuery(self):
        code = str(self.ui.lineEdit.text())
        CX = sqlite3.connect("data.db")
        CU = CX.cursor()
        CU.execute("select * from material where code = '"+code+"'")
        ans = CU.fetchall()
        if len(ans) > 0:
            single_query.go(code)
            print 'single query done.'
        else:
            reply = QMessageBox.warning(self, "single query", 'Please select an existed material code!')


    def multiQuery(self):
        code = str(self.ui.lineEdit.text())
        CX = sqlite3.connect("data.db")
        CU = CX.cursor()
        CU.execute("select * from material where code = '"+code+"'")
        ans = CU.fetchall()
        if len(ans) > 0:
            multi_query.go(code)
            print 'multi query done.'
        else:
            reply = QMessageBox.warning(self, "multi query", 'Please select an existed material code!')


    def singleReverseQuery(self):
        code = str(self.ui.lineEdit.text())
        CX = sqlite3.connect("data.db")
        CU = CX.cursor()
        CU.execute("select * from material where code = '"+code+"'")
        ans = CU.fetchall()
        if len(ans) > 0:
            single_reverse_query.go(code)
            print 'single reverse query done.'
        else:
            reply = QMessageBox.warning(self, "single reverse query", 'Please select an existed material code!')


    def multiReverseQuery(self):
        code = str(self.ui.lineEdit.text())
        CX = sqlite3.connect("data.db")
        CU = CX.cursor()
        CU.execute("select * from material where code = '"+code+"'")
        ans = CU.fetchall()
        if len(ans) > 0:
            multi_reverse_query.go(code)
            print 'multi reverse query done.'
        else:
            reply = QMessageBox.warning(self, "multi reverse query", 'Please select an existed material code!')








    def addMaterial(self):
        self.add1 = second()
        self.add1.show()

    def addRelation(self):
        self.add2 = third()
        self.add2.show()


    def deleteMaterial(self):
        selections = self.ui.tableView.selectionModel()
        selected = selections.selectedIndexes()
        if len(selected) > 0:
            reply = QMessageBox.question(self, "TABLE material", "Are you sure to delete?", QMessageBox.Yes|QMessageBox.No)
            if reply==QMessageBox.Yes:
                rowID = selected[0].row()
                self.ui.tableView.model().removeRow(rowID)
                self.model.select()
                print "del_1"
        else:
            reply = QMessageBox.warning(self, "TABLE material", 'Please select an item!')

    def deleteRelation(self):
        selections = self.ui.tableView_2.selectionModel()
        selected = selections.selectedIndexes()
        if len(selected) > 0:
            reply = QMessageBox.question(self, "TABLE relation", "Are you sure to delete?", QMessageBox.Yes|QMessageBox.No)
            if reply==QMessageBox.Yes:
                rowID = selected[0].row()
                self.ui.tableView_2.model().removeRow(rowID)
                self.model2.select()
                print "del_2"
        else:
            reply = QMessageBox.warning(self, "TABLE relation", 'Please select an item!')

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = first()
    myapp.show()
    sys.exit(app.exec_())
