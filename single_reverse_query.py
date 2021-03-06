#!/usr/bin/env python

import some_functions
import xlwt
import os



class SingleReverseQuery():
    def __init__(self):
        self.EXCEL = xlwt.Workbook()
        self.SHEET = self.EXCEL.add_sheet('single_reverse_query', cell_overwrite_ok=False)

        self.SHEET.write(0,0,r'father')
        self.SHEET.write(0,1,r'need amount')
        self.SHEET.write(0,2,r'product code')
        self.NUM = 0

    def go(self, sonCode, material, relation, product, IdToCode, CodeToId):
        if sonCode in CodeToId:
            sonId = CodeToId[sonCode]
            a = some_functions.return_Table_Column_Value('relation', 'son',str(sonId))
            if len(a)!=0:
                for i in a:
                    fatherId = i[1]
                    self.NUM += 1
                    temp1 = some_functions.return_Table_Column_Value('material', 'id', str(fatherId))
                    self.SHEET.write(self.NUM, 0, temp1[0][1])
                    self.SHEET.write(self.NUM, 1, i[3])
                    products = some_functions.findAllProduct(IdToCode[fatherId])
                    WE = ''
                    for i in products:
                        WE += '; '+i
                    WE = WE[2:]
                    self.SHEET.write(self.NUM, 2, WE)

                currentDIR = os.path.dirname(os.path.realpath(__file__))
                self.EXCEL.save(os.path.join(currentDIR, "single_reverse_query.xls"))
                print 'done'
            else:
                print 'this material has no direct father!'
        else:
            print 'no such material code!'







