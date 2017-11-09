#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql

# Open database connection
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='toshi',
                     db='testdb')
cur = conn.cursor()

# Drop table if it already exist using execute() method.
cur.execute("DROP TABLE IF EXISTS PB")

"""Creating Database Table"""
sql = """CREATE TABLE PB (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""
cur.execute(sql)

def add():
    print("OK!")
	
def exit():
	...

while(True):
    inp = input("just print something \n" )
    message = inp.split(" ")
    if message[0] == 'добавить':
        add()
	#pep-0263

    elif message[0] == 'выход':
        break
    