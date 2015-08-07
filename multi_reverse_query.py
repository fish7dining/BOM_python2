#!/usr/bin/env python

import some_functions
import xlwt
import os
import copy



class MultiReverseQuery():
    def __init__(self):
        self.EXCEL = xlwt.Workbook()
        self.SHEET = self.EXCEL.add_sheet('multi_reverse_query', cell_overwrite_ok=False)
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

            rowNum = 0
            result = {}
            for i in self.STORE1:

                #first
                temp1 = self.isColumnXYIDexisted(1, 1, rowNum, i[0][0])
                if temp1 == -1: #no exist
                    rowNum += 1
                    result[rowNum] = (1, i[0][0], i[0][1])
                    upIndex = rowNum
                    if 1 not in self.columnHash:
                        self.columnHash[1] = [(rowNum, i[0][0], i[0][1])]
                    else:
                        self.columnHash[1].append((rowNum, i[0][0], i[0][1]))
                else: #exist
                    ori1 = result[temp1]
                    result[temp1] = (ori1[0], ori1[1], ori1[2]+i[0][1])
                    upIndex = temp1

                L = len(i)
                for j in range(1,L):
                    temp1 = self.isColumnXYIDexisted(j+1, upIndex+1, rowNum, i[j][0])
                    if temp1 == -1:
                        rowNum += 1
                        result[rowNum] = (j+1, i[j][0], i[j][1])
                        upIndex = rowNum
                        if j+1 not in self.columnHash:
                            self.columnHash[j+1] = [(rowNum, i[j][0], i[j][1])]
                        else:
                            self.columnHash[j+1].append((rowNum, i[j][0], i[j][1]))
                    else:
                        oril = result[temp1]
                        result[temp1] = (oril[0], oril[1], oril[2]+i[j][1])
                        upIndex = temp1

            self.SHEET.write(0,0,r'ancestors')
            self.SHEET.write(0, MAX_IND, r'needed amount')
            self.SHEET.write(0, MAX_IND+1, r'product code')

            KK = []
            for i in range(1, rowNum+1):
                if result[i][0]==1:
                    part = result[i][1]
                    if part in product:
                        SS = IdToCode[part]
                    else:
                        pp = some_functions.findAllProduct(IdToCode[part])
                        SS = ""
                        for i in pp:
                            SS += '; '+i
                        SS = SS[2:]
                KK.append(SS)

            for i in range(1, rowNum+1):
                self.SHEET.write(i, result[i][0]-1, IdToCode[result[i][1]])
                self.SHEET.write(i, MAX_IND, str(result[i][2]))
                self.SHEET.write(i, MAX_IND+1, KK[i-1])


            currentDIR = os.path.dirname(os.path.realpath(__file__))
            self.EXCEL.save(os.path.join(currentDIR, "multi_reverse_query.xls"))
            print 'done'
        else:
            print 'no such material code!'







