#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql

# Open database connection
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       passwd='3720011',
                       db='testdb',
                       charset = "utf8",
                       use_unicode = True)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS PB")

sql = """CREATE TABLE PB (
         NUMBER CHAR(20) NOT NULL,
		 NAME  CHAR(20) NOT NULL
         )"""
cur.execute(sql)


sql = """INSERT INTO PB (NUMBER, NAME)
         VALUES ('+79221234567', 'Bob Marley')
         """
try:
    cur.execute(sql)
    print("OK!")
except:
    conn.rollback()


sql = "SELECT * FROM PB"
try:
   cur.execute(sql)
   results = cur.fetchall()
   for row in results:
      number = row[0]
      name = row[1]
      print ("number=%s,name=%s" % \
             (number, name))
except:
	print( "error: unable to fecth data")


def add():
	print("try...")
	sql = """INSERT INTO PB (NUMBER, NAME)
             VALUES ('+79221234567', 'Bob Marley')
             """
	try:
		cur.execute(sql)
		print("OK!")
	except:
		conn.rollback()

while(True):
    inp = input("just print something \n" )
    message = inp.split(" ")
    if message[0] == 'добавить':
        add()
	#pep-0263

    elif message[0] == 'выход':
        break
