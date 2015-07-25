#!/usr/bin/env python

import sqlite3
import some_functions




CX = sqlite3.connect("data.db")
CU = CX.cursor()

'''
CX.execute("create table material (id integer primary key, code varchar(20) UNIQUE, name varchar(20))")
CX.execute("create table relation (id integer primary key, father integer, son integer, ratio integer)")
'''

material = [(1,'A_1','computer'),
            (2,'A_1_1','CPU'),
            (3,'A_1_2','Memory'),
            (4,'A_1_3','screen'),
            (5,'A_1_4','mouse'),
            (6,'A_1_5','keyboard'),
            (7,'A_1_6','fan'),
            (8,'A_1_7','DisplayCard'),
            (9,'A_1_8','CDRom'),
            (10,'A_1_9','Disk'),
            (11,'A_1_5_1','click1'),
            (12,'A_1_5_2','click2'),
            (13,'A_1_5_3','click3'),
            (14,'A_1_5_2_1','he1'),
            (15,'A_1_5_3_1','he2'),
            (16,'A_1_5_3_2','he3'),
            (17,'A_1_5_3_2_1','t1'),
            ]
relation = [(1,1,2,1),
            (2,1,3,1),
            (3,1,4,1),
            (4,1,5,1),
            (5,1,6,1),
            (6,1,7,1),
            (7,1,8,1),
            (8,1,9,1),
            (9,1,10,1),

            (10,6,11,2),
            (11,6,12,3),
            (12,6,13,1),
            (13,12,14,4),
            (14,13,15,1),
            (15,13,16,2),
            (16,16,17,6),
            ]

CX.execute("delete from material")
CX.execute("delete from relation")

for t in material:
    CX.execute("insert into material values (?,?,?)",t)
CX.commit()


for t in relation:
    CX.execute("insert into relation values(?,?,?,?)",t)
CX.commit()



some_functions.printTable('material')
some_functions.printTable('relation')


