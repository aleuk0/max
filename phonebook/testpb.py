#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql

# Open database connection
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       passwd='toshi',
                       db='testdb',
                       charset = "utf8",
                       use_unicode = True)
cur = conn.cursor()

def clean():
    cur.execute("DROP TABLE IF EXISTS PB")

def create():
    sql = """CREATE TABLE PB (
            NUMBER CHAR(20) NOT NULL,
            NAME  CHAR(20) NOT NULL
            )"""
    cur.execute(sql)


def add():
    print("try...")
    sql = "INSERT INTO PB (NUMBER, NAME) VALUES ('%s', '%s')" % \
    (message[1], " ".join(message[2:]))
    try:
        cur.execute(sql)
        conn.commit()
        print("successfully commited")
    except:
        conn.rollback()

def search_all():
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
        print("error: unable to fecth data")
    
"""Найти 02
Найти Служба газа
Найти газ
Эта команда выводит всех абонентов, номер телефона или имя которых содержит приведённый текст."""
def search():
    sql = "SELECT * FROM PB WHERE NAME LIKE '%s'" % ('%'+" ".join(message[1:])+'%')
    try:
        cur.execute(sql)
        results = cur.fetchall()
        for row in results:
            number = row[0]
            name = row[1]
            print ("number=%s,name=%s" % \
                (number, name))
    except:
        print("error: unable to fecth data")
#TODO: чтобы искал и по именам, и по номерам

def delete():
    sql = "DELETE FROM PB WHERE NAME = '%s'" % (" ".join(message[1:]))
    try:
        cur.execute(sql)
        conn.commit()
    except:
        conn.rollback()


while(True):
    inp = input("just print something \n" )
    message = inp.split(" ")
    if message[0] == 'добавить':
        add()

    elif message[0] == 'найтивсех':
        search_all()
        
    elif message[0] == 'найти':
        search()

    elif message[0] == 'удалить':
        delete()

    elif message[0] == 'выход':
        break

cur.close()
conn.close()
input('successfully closed')
