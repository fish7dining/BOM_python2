#!/usr/bin/env python

import sqlite3
import some_functions
import xlwt


EXCEL = xlwt.Workbook()
SHEET = EXCEL.add_sheet('multi_reverse_query', cell_overwrite_ok=True)
NUM = 0
NUMArray = []
MAX_IND = 0

def gogo(IND, needNum, ID):
    global NUM, MAX_IND
    MAX_IND = max( MAX_IND, IND )
    direct_father = some_functions.return_Table_Column_Value('relation', 'son', str(ID))
    if len(direct_father)==0:
        return -1;
    t = 0
    for i in direct_father:
        father_name = some_functions.return_Table_Column_Value('material', 'id', str(i[1]))[0][1]
        t = gogo(IND+1, needNum*i[3], i[1])+1
        NUM += 1
        SHEET.write(NUM, t, father_name)
        NUMArray.append(needNum*i[3])
    return t


def go(sonCode):
    a = some_functions.return_Table_Column_Value('material', 'code', sonCode)
    if len(a)!=0:
        Id = a[0][0]
        gogo(0, 1, Id)
        for i in range(1,NUM+1):
            SHEET.write(i, MAX_IND, NUMArray[i-1])

        SHEET.write(0,0,r'ancestors')
        SHEET.write(0,MAX_IND,r'needed amount')
        SHEET.write(0,MAX_IND+1,r'product code')
        EXCEL.save(r'/home/valseek/PycharmProjects/bom/multi_reverse_query.xls')
        print 'done'
    else:
        print 'no such material code!'







