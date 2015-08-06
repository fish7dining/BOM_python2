#!/usr/bin/env python

import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMessageBox, QTreeWidgetItem, QDesktopWidget
from PyQt4.QtSql import QSqlDatabase, QSqlTableModel
from UI import Ui_MainWindow
from UI2 import Ui_Dialog
from UI3 import Ui_Dialog2
import sqlite3
import single_query, multi_query, single_reverse_query, multi_reverse_query, end_reverse_query
import os
import some_functions




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
        code = self.ui.lineEdit.text()
        name = self.ui.lineEdit_2.text()
        isProduct = self.ui.checkBox.isChecked()
        self.CU.execute("select * from material where code = '"+str(code)+"'")
        ans = self.CU.fetchmany(1)
        if len(ans) > 0:
            QMessageBox.warning(self, "Wrong", 'Code Name has already exist!')
        else:
            self.CU.execute("insert into material values(?,?,?,?)",(None, str(code), str(name), isProduct))
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

    def add(self):
        if self.ui.lineEdit.text() != '':
            fatherID = myapp.MATERIAL_code_id[str(self.ui.comboBox.currentText())]
            sonID = myapp.MATERIAL_code_id[str(self.ui.comboBox_2.currentText())]
            ratios = int(self.ui.lineEdit.text())
            self.CU.execute("select * from relation where father = '"+str(fatherID)+ \
                       "' and son = '"+str(sonID)+"'")
            ans = self.CU.fetchmany(1)
            if len(ans)==0:
                self.CU.execute("insert into relation values(?,?,?,?)",(None, fatherID, sonID, ratios))
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
        self.MATERIAL = self.CU.fetchall()
        self.MATERIAL_id_code = {}
        self.MATERIAL_code_id = {}
        self.PRODUCT = []
        for i in self.MATERIAL:
            self.MATERIAL_id_code[i[0]] = str(i[1])
            self.MATERIAL_code_id[str(i[1])] = i[0]
            if i[3]==True:
                self.PRODUCT.append(i[1])
        self.CU.execute("select * from relation")
        self.RELATION = self.CU.fetchall()

    #update treeWdigets
    def update_tree(self):
        self.ui.treeWidget.clear()
        self.ui.treeWidget_2.clear()
        self.tree1Item = []
        self.tree2Item = {}
        for i in self.MATERIAL:
            self.tree1Item.append(QTreeWidgetItem(self.tree1))
            self.tree1Item[-1].setText(0, str(i[1]))
            self.tree1Item[-1].setText(1, str(i[2]))
            if i[3]==1:
                self.tree1Item[-1].setText(2, 'True')
        for i in self.RELATION:
            fatherID = i[1]
            fatherCode = self.MATERIAL_id_code[fatherID]
            sonID = i[2]
            sonCode = self.MATERIAL_id_code[sonID]
            ratio = i[3]

            if fatherID not in self.tree2Item:
                self.tree2Item[fatherID] = QTreeWidgetItem(self.tree2)
                self.tree2Item[fatherID].setText(0, fatherCode)
                if some_functions.return_Table_Column_Value('material', 'id', str(some_functions.code_to_id(fatherCode)))[0][3]==True:
                    self.tree2Item[fatherID].setText(2, fatherCode)
            key = (fatherID, sonID)
            if key not in self.tree2Item:
                self.tree2Item[key] = QTreeWidgetItem(self.tree2Item[fatherID])
                self.tree2Item[key].setText(0, sonCode)
                self.tree2Item[key].setText(1, str(ratio))

    def MoveToScreenCenter(self):
        screen = QDesktopWidget().screenGeometry()
        mysize = self.geometry()
        hpos = ( screen.width() - mysize.width() ) / 2
        vpos = ( screen.height() - mysize.height() ) / 2
        self.move(hpos, vpos)

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.MoveToScreenCenter()

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
        self.tree1.setColumnCount(3)
        self.tree1.setHeaderLabels(['Code','Name','IsProduct'])
        self.tree2 = self.ui.treeWidget_2
        self.tree2.setColumnCount(2)
        self.tree2.setHeaderLabels(['Code', 'Ratio', 'Product'])
        #----------------------------------------------------------------------------

        self.update_memory()
        self.update_tree()


        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL("clicked()"), self.deleteMaterial)
        QtCore.QObject.connect(self.ui.pushButton_4, QtCore.SIGNAL("clicked()"), self.deleteRelation)
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.addMaterial)
        QtCore.QObject.connect(self.ui.pushButton_3, QtCore.SIGNAL("clicked()"), self.addRelation)

        QtCore.QObject.connect(self.ui.pushButton_5, QtCore.SIGNAL("clicked()"), self.singleQuery)
        QtCore.QObject.connect(self.ui.pushButton_6, QtCore.SIGNAL("clicked()"), self.multiQuery)
        QtCore.QObject.connect(self.ui.pushButton_7, QtCore.SIGNAL("clicked()"), self.singleReverseQuery)
        QtCore.QObject.connect(self.ui.pushButton_8, QtCore.SIGNAL("clicked()"), self.multiReverseQuery)
        QtCore.QObject.connect(self.ui.pushButton_9, QtCore.SIGNAL("clicked()"), self.endReverseQuery)


    def singleQuery(self):
        code = str(self.ui.lineEdit.text())
        self.CU.execute("select * from material where code = '"+code+"'")
        ans = self.CU.fetchmany(1)
        if len(ans) > 0:
            single_query.SingleQuery().go(code, self.MATERIAL, self.RELATION, self.PRODUCT, \
                                          self.MATERIAL_id_code, self.MATERIAL_code_id)
            QMessageBox.warning(self, "single query", 'EXCEL generated successfully')
        else:
            QMessageBox.warning(self, "single query", 'Please select an existed material code!')


    def multiQuery(self):
        code = str(self.ui.lineEdit.text())
        self.CU.execute("select * from material where code = '"+code+"'")
        ans = self.CU.fetchmany(1)
        if len(ans) > 0:
            multi_query.MultiQuery().go(code, self.MATERIAL, self.RELATION, self.PRODUCT, \
                                        self.MATERIAL_id_code, self.MATERIAL_code_id)
            QMessageBox.warning(self, "multi query", 'EXCEL generated successfully')
        else:
            QMessageBox.warning(self, "multi query", 'Please select an existed material code!')


    def singleReverseQuery(self):
        code = str(self.ui.lineEdit.text())
        self.CU.execute("select * from material where code = '"+code+"'")
        ans = self.CU.fetchmany(1)
        if len(ans) > 0:
            single_reverse_query.SingleReverseQuery().go(code, self.MATERIAL, self.RELATION, self.PRODUCT, \
                                                         self.MATERIAL_id_code, self.MATERIAL_code_id)
            QMessageBox.warning(self, "single reverse query", 'EXCEL generated successfully')
        else:
            QMessageBox.warning(self, "single reverse query", 'Please select an existed material code!')


    def multiReverseQuery(self):
        code = str(self.ui.lineEdit.text())
        self.CU.execute("select * from material where code = '"+code+"'")
        ans = self.CU.fetchmany(1)
        if len(ans) > 0:
            multi_reverse_query.MultiReverseQuery().go(code, self.MATERIAL, self.RELATION, self.PRODUCT, \
                                                       self.MATERIAL_id_code, self.MATERIAL_code_id)
            QMessageBox.warning(self, "multi reverse query", 'EXCEL generated successfully')
        else:
            QMessageBox.warning(self, "multi reverse query", 'Please select an existed material code!')


    def endReverseQuery(self):
        code = str(self.ui.lineEdit.text())
        self.CU.execute("select * from material where code = '"+code+"'")
        ans = self.CU.fetchmany(1)
        if len(ans) > 0:
            end_reverse_query.EndReverseQuery().go(code, self.MATERIAL, self.RELATION, self.PRODUCT, \
                                                   self.MATERIAL_id_code, self.MATERIAL_code_id)
            QMessageBox.warning(self, "end reverse query", 'EXCEL generated successfully')
        else:
            QMessageBox.warning(self, "end reverse query", 'Please select an existed material code!')


    def addMaterial(self):
        add1 = second()
        add1.exec_()

    def addRelation(self):
        add2 = third()
        add2.exec_()

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
                reply = QMessageBox.question(self, "TABLE relation", "Are you sure to delete?", QMessageBox.Yes|QMessageBox.No)
                if reply==QMessageBox.Yes:
                    parent = selections[0].parent()
                    fatherID = self.MATERIAL_code_id[str(parent.text(0))]
                    sonID = self.MATERIAL_code_id[str(selections[0].text(0))]
                    self.CU.execute("delete from relation where father = '"+str(fatherID)+"' and son = '"+str(sonID)+"'")
                    self.CX.commit()
                    self.update_memory()
                    self.update_tree()
            else:
                QMessageBox.warning(self, "ERROR", 'Please delete its children!')




if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = first()
    myapp.show()
    sys.exit(app.exec_())
