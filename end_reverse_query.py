#!/usr/bin/env python

import some_functions
import xlwt
import os
import copy



class EndReverseQuery():
    def __init__(self):
        self.EXCEL = xlwt.Workbook()
        self.SHEET = self.EXCEL.add_sheet('end_reverse_query', cell_overwrite_ok=False)
        self.STORE1 = []
        self.columnHash = {}

    def findAllFatherID(self, sonID):
        a1 = some_functions.return_Table_Column_Value('relation', 'son', str(sonID))
        ans = []
        for i in a1:
            ans.append((i[1], i[3]))  #i[1]:father  i[3]:ratio
        return ans

    def gogo(self, sonID, K):
        if K not in self.STORE1:
            self.STORE1.append(K)
        fatherIDs = self.findAllFatherID(sonID)
        for i in fatherIDs:
            newK = copy.deepcopy(K)
            newK.append((i[0],K[-1][1]*i[1]))
            self.gogo(i[0], newK)

    def isColumnXYIDexisted(self, columnIndex, x, y, ID):
        if x > y or (columnIndex not in self.columnHash):
            return -1
        X = self.columnHash[columnIndex]
        for i in X:
            if i[1] == ID and i[0] >= x and i[0] <= y:
                return i[0]
        return -1

    def mycmp(self, x, y):
        L = min( len(x), len(y) )
        for i in range(L):
            if x[i][0] > y[i][0]:
                return 1
            elif x[i][0] == y[i][0]:
                continue
            else:
                return -1

    def go(self, sonCode, material, relation, product, IdToCode, CodeToId):
        if sonCode in CodeToId:
            sonId = CodeToId[sonCode]
            self.STORE1 = []
            self.gogo(sonId, [(sonId,1)])
            self.STORE1.pop(self.STORE1.index([(sonId, 1)]))
            MAX_IND = 0
            for i in self.STORE1:
                i.reverse()
                MAX_IND = max(MAX_IND, len(i))
            self.STORE1.sort(cmp = self.mycmp)

            DIC = {}
            for i in self.STORE1:
                if IdToCode[i[0][0]] in product:
                    if i[0][0] not in DIC:
                        DIC[i[0][0]] = i[0][1]
                    else:
                        DIC[i[0][0]] += i[0][1]

            self.SHEET.write(0,0,r'end product')
            self.SHEET.write(0, 1, r'needed amount')
            self.SHEET.write(0, 2, r'product code')

            ROW = 0
            for key in DIC.keys():
                ROW += 1
                self.SHEET.write(ROW, 0, IdToCode[key])
                self.SHEET.write(ROW, 1, DIC[key])
                self.SHEET.write(ROW, 2, IdToCode[key])

            currentDIR = os.path.dirname(os.path.realpath(__file__))
            self.EXCEL.save(os.path.join(currentDIR, "end_reverse_query.xls"))
            print 'done'
        else:
            print 'no such material code!'







