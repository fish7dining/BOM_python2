#!/usr/bin/env python

import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMessageBox, QTreeWidgetItem
from PyQt4.QtSql import QSqlDatabase, QSqlTableModel
from UI import Ui_MainWindow
from UI2 import Ui_Dialog
from UI3 import Ui_Dialog2
import sqlite3
import single_query, multi_query, single_reverse_query, multi_reverse_query
import os




class second(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.bye)
        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL("clicked()"), self.add)
        self.CX = sqlite3.connect("data.db")
        self.CU = self.CX.cursor()

    def add(self):
        code = self.ui.textEdit.toPlainText()
        name = self.ui.textEdit_2.toPlainText()
        self.CU.execute("select * from material where code = '"+str(code)+"'")
        ans = self.CU.fetchmany(1)
        if len(ans) > 0:
            QMessageBox.warning(self, "Wrong", 'Code Name has already exist!')
        else:
            self.CU.execute("insert into material values(?,?,?)",(None, str(code), str(name)))
            self.CX.commit()
            myapp.update_memory()
            myapp.update_tree()
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
        self.CX = sqlite3.connect("data.db")
        self.CU = self.CX.cursor()
        for i in myapp.MATERIAL:
            self.ui.comboBox.addItem(str(i[1]))
            self.ui.comboBox_2.addItem(str(i[1]))
            self.ui.comboBox_3.addItem(str(i[1]))
    def add(self):
        if self.ui.lineEdit.text() != '':
            fatherID = myapp.MATERIAL_code_id[str(self.ui.comboBox.currentText())]
            sonID = myapp.MATERIAL_code_id[str(self.ui.comboBox_2.currentText())]
            productID = myapp.MATERIAL_code_id[str(self.ui.comboBox_3.currentText())]
            ratios = int(self.ui.lineEdit.text())
            self.CU.execute("select * from relation where father = '"+str(fatherID)+ \
                       "' and son = '"+str(sonID)+"' and productID = '"+str(productID)+"'")
            ans = self.CU.fetchmany(1)
            if len(ans)==0:
                self.CU.execute("insert into relation values(?,?,?,?,?)",(None, fatherID, sonID, ratios, productID))
                self.CX.commit()
                myapp.update_memory()
                myapp.update_tree()
                self.close()
            else:
                QMessageBox.warning(self, "TABLE relation", 'Has already existed!')
        else:
            QMessageBox.warning(self, "TABLE relation", 'ratio is empty!')

    def bye(self):
        self.close()





class first(QtGui.QMainWindow):

    #update map [database -> memory]
    def update_memory(self):
        self.CU.execute("select * from material")
        self.MATERIAL = self.CU.fetchmany(50)
        self.MATERIAL_id_code = {}
        self.MATERIAL_code_id = {}
        for i in self.MATERIAL:
            self.MATERIAL_id_code[i[0]] = str(i[1])
            self.MATERIAL_code_id[str(i[1])] = i[0]

        self.CU.execute("select * from relation")
        self.RELATION = self.CU.fetchmany(50)

    #update treeWdigets
    def update_tree(self):
        self.ui.treeWidget.clear()
        self.ui.treeWidget_2.clear()
        self.tree1Item = []
        self.tree2Item = {}
        for i in self.MATERIAL:
            self.tree1Item.append(QTreeWidgetItem(self.tree1))
            self.tree1Item[len(self.tree1Item)-1].setText(0, str(i[1]))
            self.tree1Item[len(self.tree1Item)-1].setText(1, str(i[2]))
        for i in self.RELATION:
            ID = i[0]
            fatherID = i[1]
            fatherCode = self.MATERIAL_id_code[fatherID]
            sonID = i[2]
            sonCode = self.MATERIAL_id_code[sonID]
            ratio = i[3]
            productID = i[4]
            productCode = self.MATERIAL_id_code[productID]

            if fatherID not in self.tree2Item:
                self.tree2Item[fatherID] = QTreeWidgetItem(self.tree2)
                self.tree2Item[fatherID].setText(0, fatherCode)
                self.tree2Item[fatherID].setText(2, productCode)
            key = (fatherID, sonID, productID)
            if key not in self.tree2Item:
                self.tree2Item[key] = QTreeWidgetItem(self.tree2Item[fatherID])
                self.tree2Item[key].setText(0, sonCode)
                self.tree2Item[key].setText(1, str(ratio))
                self.tree2Item[key].setText(2, productCode)



    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #-stable---------------------------------------------------------------------------
        self.currentDIR = os.path.dirname(os.path.realpath(__file__))

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(os.path.join(self.currentDIR, "data.db"))
        if self.db.open():
            print "Open data.db successfully"
        else:
            print "Could not open data.db"
        self.CX = sqlite3.connect("data.db")
        self.CU = self.CX.cursor()

        self.tree1 = self.ui.treeWidget
        self.tree1.setColumnCount(2)
        self.tree1.setHeaderLabels(['Code','Name'])
        self.tree2 = self.ui.treeWidget_2
        self.tree2.setColumnCount(3)
        self.tree2.setHeaderLabels(['Code', 'Ratio', 'Product'])
        #----------------------------------------------------------------------------

        self.update_memory()
        self.update_tree()




        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL("clicked()"), self.deleteMaterial)
        QtCore.QObject.connect(self.ui.pushButton_4, QtCore.SIGNAL("clicked()"), self.deleteRelation)
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.addMaterial)
        QtCore.QObject.connect(self.ui.pushButton_3, QtCore.SIGNAL("clicked()"), self.addRelation)

        '''
        QtCore.QObject.connect(self.ui.pushButton_5, QtCore.SIGNAL("clicked()"), self.singleQuery)
        QtCore.QObject.connect(self.ui.pushButton_6, QtCore.SIGNAL("clicked()"), self.multiQuery)
        QtCore.QObject.connect(self.ui.pushButton_7, QtCore.SIGNAL("clicked()"), self.singleReverseQuery)
        QtCore.QObject.connect(self.ui.pushButton_8, QtCore.SIGNAL("clicked()"), self.multiReverseQuery)
        #QtCore.QObject.connect(self.ui.pushButton_9, QtCore.SIGNAL("clicked()"), self.deleteRelation)
        '''
    '''
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

    '''

    def addMaterial(self):
        self.add1 = second()
        self.add1.exec_()

    def addRelation(self):
        self.add2 = third()
        self.add2.exec_()

    def deleteMaterial(self):
        selections = self.tree1.selectedItems()
        if len(selections) > 0:
            Code = str(selections[0].text(0))
            reply = QMessageBox.question(self, "TABLE material", "Are you sure to delete?", QMessageBox.Yes|QMessageBox.No)
            if reply==QMessageBox.Yes:
                self.CU.execute("select * from relation where father = "+str(self.MATERIAL_code_id[Code])+\
                                " or son = "+str(self.MATERIAL_code_id[Code]))
                ans = self.CU.fetchmany(1)
                if len(ans) > 0:
                    QMessageBox.warning(self, "ERROR", 'Please first clean TABLE relation!')
                else:
                    self.CU.execute("delete from material where code = '"+Code+"'")
                    self.CX.commit()
                    self.update_memory()
                    self.update_tree()


    def deleteRelation(self):
        selections = self.tree2.selectedItems()
        if len(selections) > 0:
            ratio = str(selections[0].text(1))
            if ratio != '':
                parent = selections[0].parent()
                fatherID = self.MATERIAL_code_id[str(parent.text(0))]
                sonID = self.MATERIAL_code_id[str(selections[0].text(0))]
                productID = self.MATERIAL_code_id[str(selections[0].text(2))]
                self.CU.execute("delete from relation where father = '"+str(fatherID)+"' and son = '"+str(sonID)+\
                                "' and productID = '"+str(productID)+"'")
                self.CX.commit()
                self.update_memory()
                self.update_tree()




if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = first()
    myapp.show()
    sys.exit(app.exec_())
