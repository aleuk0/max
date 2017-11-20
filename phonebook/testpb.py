#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql

# TODO: написать 4 теста, проверяющих реализации команд.

# Open database connection
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       passwd='3720011',
                       db='testdb',
                       charset="utf8",
                       use_unicode=True)
cur = conn.cursor()


def create_new_phonebook():
    cur.execute("DROP TABLE IF EXISTS PB")
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


def search():
    sql = "SELECT * FROM PB WHERE NAME LIKE '%s' OR NUMBER LIKE '%s'" % \
          ('%' + " ".join(message[1:]) + '%', '%' + " ".join(message[1:]) + '%')
    try:
        cur.execute(sql)
        results = cur.fetchall()
        for row in results:
            number = row[0]
            name = row[1]
            print("number=%s,name=%s" % \
                  (number, name))
    except:
        print("error: unable to fecth data")


def delete():
    sql = "DELETE FROM PB WHERE NAME = '%s' OR NUMBER = '%s'" % \
          (" ".join(message[1:]), " ".join(message[1:]))
    try:
        cur.execute(sql)
        conn.commit()
    except:
        conn.rollback()


while True:
    inp = input("""Телефонный справочник.
Поддерживает команды: найти, добавить, удалить, выход. 
Введите команду: \n
""")
    message = inp.split(" ")
    if message[0] == 'добавить':
        add()
    elif message[0] == 'найти':
        search()
    elif message[0] == 'удалить':
        delete()
    elif message[0] == 'выход':
        break
    print("\n")

cur.close()
conn.close()
input('successfully closed')
