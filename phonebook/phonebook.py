#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql


"""При реализации этой программы необходимо создать
1. Интерфейс или абстрактный класс команды ICommand. Класс команды содержит один метод: выполнить команду,
 в качестве аргументов принимает строку, которая вызвала выполнение команды
2. Фасадный класс цикла обработки команд CommandLoop который содержит единственный публичный метод DoLoop(),
 который выполняется до тех пор, пока не будет вызвана команда Выход. Содержит внутри себя экземпляры классов
  фабрики команд и списка телефонов (List<класс данных>).
3. Класс данных который содержит два строковых поля: номер телефона и название абонента
4. Фабрику команд CommandFactory, которая принимает строку для выполнения и объект CommandLoop, а возвращает
 объект команды. Фабрика читает первую часть строки и выбирает конкретную реализацию команды. Команды могут
  обратиться к CommandLoop для перечитывания списка телефонов или сообщений циклу о том, что чтение команд
   необходимо прекратить и завершить DoLoop().
5. 4 класс реализующих команды Добавить, Найти, Удалить и Выход."""


# Open database connection
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       passwd='toshi',
                       db='testdb',
                       charset="utf8",
                       use_unicode=True)
cur = conn.cursor()

"""В консоли программа принимает следующие команды:
Добавить +79058023741 Бородин А.М.
Добавить 02 Полиция
Добавить 04 Служба газа
Эта команда добавляет в справочник соответствующее телефону ФИО. Телефон не содержит пробелов."""


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


"""Найти 02
Найти Служба газа
Найти газ
Эта команда выводит всех абонентов, номер телефона или имя которых содержит приведённый текст."""


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


"""Удалить 02
Удалить Бородин А.М.
Эта команда удаляет запись, телефон или название которой строго соответствует аргументу."""


def delete():
    sql = "DELETE FROM PB WHERE NAME = '%s' OR NUMBER = '%s'" % \
          (" ".join(message[1:]), " ".join(message[1:]))
    try:
        cur.execute(sql)
        conn.commit()
    except:
        conn.rollback()


"""Выход
Эта команда сообщает системе что нужно прекратить принимать команды и завершить выполнение приложения."""


def exit():
    ...


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
