#!/usr/bin/env python

import some_functions
import xlwt
import os


class MultiQuery():
    def __init__(self):
        self.EXCEL = xlwt.Workbook()
        self.SHEET = self.EXCEL.add_sheet('multi_query', cell_overwrite_ok=False)
        self.NUM = 0
        self.NUMArray = []
        self.MAX_IND = 0

    def gogo(self, IND, needNum, ID):
        self.MAX_IND = max( self.MAX_IND, IND )
        direct_son = some_functions.return_Table_Column_Value('relation', 'father', str(ID))
        for i in direct_son:
            self.NUM += 1
            son_code = some_functions.return_Table_Column_Value('material', 'id', str(i[2]))[0][1]
            self.SHEET.write(self.NUM, IND, son_code)
            self.NUMArray.append(needNum*i[3])
            self.gogo(IND+1, needNum*i[3], i[2])

    def go(self, fatherCode, material, relation, product, IdToCode, CodeToId):
        if fatherCode in CodeToId:
            fatherId = CodeToId[fatherCode]
            self.gogo(0, 1, fatherId)
            products = some_functions.findAllProduct(fatherCode) #return fatherCode's all products
            WE = ''
            for i in products:
                WE += '; '+i
            WE = WE[2:]
            for i in range(1,self.NUM+1):
                self.SHEET.write(i, self.MAX_IND, self.NUMArray[i-1])
                self.SHEET.write(i, self.MAX_IND+1, WE)
            self.SHEET.write(0,0,r'descendants')
            self.SHEET.write(0,self.MAX_IND,r'needed amount')
            self.SHEET.write(0,self.MAX_IND+1,r'product code')

            currentDIR = os.path.dirname(os.path.realpath(__file__))
            self.EXCEL.save(os.path.join(currentDIR, "multi_query.xls"))
            print 'done'
        else:
            print 'no such material code!'







