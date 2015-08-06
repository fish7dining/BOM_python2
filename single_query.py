#!/usr/bin/env python

import some_functions
import xlwt
import os
import app

class SingleQuery():
    def go(self, fatherCode, material, relation, product, IdToCode, CodeToId):
        self.EXCEL = xlwt.Workbook()
        self.SHEET = self.EXCEL.add_sheet('single_query', cell_overwrite_ok=False)

        self.SHEET.write(0,0,r'direct son')
        self.SHEET.write(0,1,r'needed amount')
        self.SHEET.write(0,2,r'product code')
        self.NUM = 0

        if fatherCode in CodeToId:
            fatherId = CodeToId[fatherCode]
            a = some_functions.return_Table_Column_Value('relation', 'father',str(fatherId))
            products = some_functions.findAllProduct(fatherCode) #return fatherCode's all products
            WE = ''
            for i in products:
                WE += '; '+i
            WE = WE[2:]

            if len(a)!=0:
                for i in a:
                    sonId = i[2]
                    self.NUM += 1
                    temp1 = some_functions.return_Table_Column_Value('material', 'id', str(sonId))
                    self.SHEET.write(self.NUM, 0, temp1[0][1])
                    self.SHEET.write(self.NUM, 1, i[3])
                    self.SHEET.write(self.NUM, 2, WE)

                currentDIR = os.path.dirname(os.path.realpath(__file__))
                self.EXCEL.save(os.path.join(currentDIR, "single_query.xls"))
                print 'done'
            else:
                print 'this material has no direct son!'
                currentDIR = os.path.dirname(os.path.realpath(__file__))
                self.EXCEL.save(os.path.join(currentDIR, "single_query.xls"))
                print 'done'
        else:
            print 'no such material code!'








