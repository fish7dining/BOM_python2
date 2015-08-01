#!/usr/bin/env python

import sqlite3

#print every record in talbe 'names'
def printTable(names):
    CX = sqlite3.connect("data.db")
    CU = CX.cursor()

    CU.execute("select * from "+names)
    a = CU.fetchall()
    for i in a:
        print i

    CU.close()
    CX.close()

#return record set in [TableName, ColumnName, Values]
def return_Table_Column_Value(TableName, ColumnName, Values):
    CX = sqlite3.connect("data.db")
    CU = CX.cursor()

    CU.execute("select * from "+TableName+" where "+ColumnName+" = '"+Values+"'")
    ans = CU.fetchall()

    return ans
