#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#pep-0263

import pymysql

# Open database connection
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='toshi',
                     db='testdb')
cur = conn.cursor()

def newpb():
	# Drop table if it already exist using execute() method.
	cur.execute("DROP TABLE IF EXISTS PB")

	"""Creating Database Table"""
	sql = """CREATE TABLE PB (
			 NUMBER CHAR(20) NOT NULL,
			 NAME  CHAR(20) NOT NULL
			 )"""
	cur.execute(sql)

"""В консоли программа принимает следующие команды:
Добавить +79058023741 Бородин А.М.
Добавить 02 Полиция
Добавить 04 Служба газа
Эта команда добавляет в справочник соответствующее телефону ФИО. Телефон не содержит пробелов."""
def add():
    ...

"""Найти 02
Найти Служба газа
Найти газ
Эта команда выводит всех абонентов, номер телефона или имя которых содержит приведённый текст."""
def search():
    ...

"""Удалить 02
Удалить Бородин А.М.
Эта команда удаляет запись, телефон или название которой строго соответствует аргументу."""
def delete():
    ...

"""Выход
Эта команда сообщает системе что нужно прекратить принимать команды и завершить выполнение приложения."""
def exit():
    ...

while(True):
    inp = input("just print something \n" )
    message = inp.split(" ")
    if message[0] == 'добавить':
        add()
	
    elif message[0] == 'выход':
        break
    




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
