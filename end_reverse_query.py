#!/usr/bin/env python

import some_functions
import xlwt
import os




class EndReverseQuery():
    def __init__(self):
        self.EXCEL = xlwt.Workbook()
        self.SHEET = self.EXCEL.add_sheet('end_reverse_query', cell_overwrite_ok=False)
        self.NUM = 0
        self.NUMArray = []
        self.productCodeArray = []
        self.MAX_IND = 0

    def gogo(self, IND, needNum, ID):
        self.MAX_IND = max( self.MAX_IND, IND )
        direct_father = some_functions.return_Table_Column_Value('relation', 'son', str(ID))
        if len(direct_father)==0:
            return -1;
        t = 0
        for i in direct_father:
            father_name = some_functions.return_Table_Column_Value('material', 'id', str(i[1]))[0][1]
            t = self.gogo(IND+1, needNum*i[3], i[1])+1
            if t==0:
                self.NUM += 1
                self.SHEET.write(self.NUM, t, father_name)
                self.NUMArray.append(needNum*i[3])
                temp1 = some_functions.return_Table_Column_Value('material', 'id', str(i[4]))
                self.productCodeArray.append(temp1[0][1])
        return t


    def go(self, sonCode):
        a = some_functions.return_Table_Column_Value('material', 'code', sonCode)
        if len(a)!=0:
            sonId = a[0][0]
            self.gogo(0, 1, sonId)
            for i in range(1,self.NUM+1):
                self.SHEET.write(i, 1, self.NUMArray[i-1])
                self.SHEET.write(i, 2, self.productCodeArray[i-1])
            self.SHEET.write(0,0,r'end product')
            self.SHEET.write(0,1,r'needed amount')
            self.SHEET.write(0,2,r'product code')

            currentDIR = os.path.dirname(os.path.realpath(__file__))
            self.EXCEL.save(os.path.join(currentDIR, "end_reverse_query.xls"))
            print 'done'
        else:
            print 'no such material code!'







