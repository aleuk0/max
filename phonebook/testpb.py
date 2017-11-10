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
         NUMBER CHAR(20) NOT NULL,
		 NAME  CHAR(20) NOT NULL
         )"""
cur.execute(sql)

def add():
	print("try")
	"""INSERT Operation"""
	sql = """INSERT INTO EMPLOYEE(NUMBER, NAME)
         VALUES ('+79221234567', 'Иван Петров')"""
	try:
		cur.execute(sql)
		print("OK!")
	except:
		conn.rollback()
	
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
    