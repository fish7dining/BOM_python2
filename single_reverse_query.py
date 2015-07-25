#!/usr/bin/env python

import sqlite3
import some_functions
import xlwt


EXCEL = xlwt.Workbook()
SHEET = EXCEL.add_sheet('single_reverse_query', cell_overwrite_ok=True)



SHEET.write(0,0,r'father')
SHEET.write(0,1,r'need amount')
SHEET.write(0,2,r'product code')
NUM = 0


fatherCode = raw_input()
a = some_functions.return_Table_Column_Value('material', 'code', fatherCode)
if len(a)!=0:
    Id = a[0][0]
    a = some_functions.return_Table_Column_Value('relation', 'son',str(Id))
    if len(a)!=0:
        CodeMap = {}
        for i in a:
            Id2 = i[1]
            NUM += 1
            if Id2 in CodeMap:
                SHEET.write(NUM, 0, CodeMap[Id2])
            else:
                temp1 = some_functions.return_Table_Column_Value('material', 'id', str(Id2))
                SHEET.write(NUM, 0, temp1[0][1])
                SHEET.write(NUM, 1, i[3])
                CodeMap[Id2] = temp1[0][1];
        EXCEL.save(r'/home/valseek/PycharmProjects/bom/single_reverse_query.xls')
        print 'done'
    else:
        print 'this material has no direct father!'
else:
    print 'no such material code!'







