#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql

message = []

# Open database connection
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       passwd='toshi',
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


def add(message):
    #print("try...")
    sql = "INSERT INTO PB (NUMBER, NAME) VALUES ('%s', '%s')" % \
          (message[1], " ".join(message[2:]))
    try:
        cur.execute(sql)
        conn.commit()
        #print("successfully commited")
    except:
        conn.rollback()


def search(message):
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


def delete(message):
    sql = "DELETE FROM PB WHERE NAME = '%s' OR NUMBER = '%s'" % \
          (" ".join(message[1:]), " ".join(message[1:]))
    try:
        cur.execute(sql)
        conn.commit()
    except:
        conn.rollback()

def close_db():
    cur.close()
    conn.close()
    #input('successfully closed')

if __name__ == "__main__":
    while True:
        inp = input("""Телефонный справочник.
    Поддерживает команды: найти, добавить, удалить, выход. 
    Введите команду: \n
    """)
        message = inp.split(" ")
        if message[0] == 'добавить':
            add(message)
        elif message[0] == 'найти':
            search(message)
        elif message[0] == 'удалить':
            delete(message)
        elif message[0] == 'выход':
            break
        print("\n")
        
    close_db()
