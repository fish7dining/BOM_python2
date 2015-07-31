#!/usr/bin/env python

import sqlite3
import some_functions
import xlwt

EXCEL = xlwt.Workbook()
SHEET = EXCEL.add_sheet('multi_query', cell_overwrite_ok=True)

NUM = 0
NUMArray = []
MAX_IND = 0

def gogo(IND, needNum, ID):
    global NUM, MAX_IND
    MAX_IND = max( MAX_IND, IND )
    direct_son = some_functions.return_Table_Column_Value('relation', 'father', str(ID))
    for i in direct_son:
        NUM += 1
        son_name = some_functions.return_Table_Column_Value('material', 'id', str(i[2]))[0][1]
        SHEET.write(NUM, IND, son_name)
        NUMArray.append(needNum*i[3])
        gogo(IND+1, needNum*i[3], i[2])


def go(fatherCode):
    a = some_functions.return_Table_Column_Value('material', 'code', fatherCode)
    if len(a)!=0:
        Id = a[0][0]
        gogo(0, 1, Id)
        for i in range(1,NUM+1):
            SHEET.write(i, MAX_IND, NUMArray[i-1])
        SHEET.write(0,0,r'descendants')
        SHEET.write(0,MAX_IND,r'needed amount')
        SHEET.write(0,MAX_IND+1,r'product code')
        EXCEL.save(r'/home/valseek/PycharmProjects/bom/multi_query.xls')
        print 'done'
    else:
        print 'no such material code!'







