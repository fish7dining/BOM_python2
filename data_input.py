#!/usr/bin/env python

import sqlite3
import some_functions





'''
cu.execute("create table material (id integer primary key, code varchar(20) UNIQUE, name varchar(20))")
cu.execute("create table relation (id integer primary key, father integer, son integer, ratio integer)")
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
            ]
'''
for t in material:
    CX.execute("insert into material values (?,?,?)",t)
CX.commit()
'''
'''
for t in relation:
    CX.execute("insert into relation values(?,?,?,?)",t)
CX.commit()
'''


some_functions.printTable('material')
some_functions.printTable('relation')


