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

def code_to_id(code):
    CX = sqlite3.connect("data.db")
    CU = CX.cursor()
    CU.execute("select * from material where code = '"+str(code)+"'")
    ans = CU.fetchall()
    if len(ans) == 0:
        return -1
    else:
        return int(ans[0][0])

def id_to_code(id):
    CX = sqlite3.connect("data.db")
    CU = CX.cursor()
    CU.execute("select * from material where id = '"+str(id)+"'")
    ans = CU.fetchall()
    if len(ans) == 0:
        return ''
    else:
        return str(ans[0][1])

#find all products which code belongs to
def findAllProduct(code):
    CX = sqlite3.connect("data.db")
    CU = CX.cursor()
    CU.execute("select * from relation where son = '"+str(code_to_id(code))+"'")
    ans = CU.fetchall()
    if len(ans) == 0:
        return [code]
    else:
        res = []
        for i in ans:
            t = findAllProduct(id_to_code(int(i[1])))
            for j in t:
                if j not in res:
                    res.append(j)
        return res











