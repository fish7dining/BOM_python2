#!/usr/bin/env python

import sqlite3
import some_functions
import xlwt


def go(fatherCode):
    EXCEL = xlwt.Workbook()
    SHEET = EXCEL.add_sheet('single_query', cell_overwrite_ok=True)

    SHEET.write(0,0,r'son')
    SHEET.write(0,1,r'needed amount')
    SHEET.write(0,2,r'product code')
    NUM = 0

    a = some_functions.return_Table_Column_Value('material', 'code', fatherCode)
    if len(a)!=0:
        Id = a[0][0]
        a = some_functions.return_Table_Column_Value('relation', 'father',str(Id))
        if len(a)!=0:
            CodeMap = {}
            for i in a:
                Id2 = i[2]
                NUM += 1
                if Id2 in CodeMap:
                    SHEET.write(NUM, 0, CodeMap[Id2])
                else:
                    temp1 = some_functions.return_Table_Column_Value('material', 'id', str(Id2))
                    SHEET.write(NUM, 0, temp1[0][1])
                    SHEET.write(NUM, 1, i[3])
                    CodeMap[Id2] = temp1[0][1];
            EXCEL.save(r'/home/valseek/PycharmProjects/bom/single_query.xls')
            print 'done'
        else:
            print 'this material has no direct son!'
    else:
        print 'no such material code!'







