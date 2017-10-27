#!/usr/bin/env python
#https://www.tutorialspoint.com/python/python_database_access.htm
#https://stackoverflow.com/questions/35684400/how-to-use-python-3-5-1-with-a-mysql-database

import pymysql

# Open database connection
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='toshi',
                     conn='TESTDB')
cur = conn.cursor()

# Drop table if it already exist using execute() method.
cur.execute("DROP TABLE IF EXISTS EMPLOYEE")

"""Creating Database Table"""
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""
cur.execute(sql)


"""INSERT Operation"""
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
	cur.execute(sql)
except:
	conn.rollback()


"""READ Operation"""
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)
try:
   cur.execute(sql)
   results = cur.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      print ("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, sex, income ))
except:
	print( "error: unable to fecth data")


"""Update Operation"""
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
   cur.execute(sql)
   conn.commit()
except:
   conn.rollback()


"""Delete Operation"""
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
try:
   cur.execute(sql)
   conn.commit()
except:
   conn.rollback()


cur.execute("SELECT * FROM users")
print(cur.description)
for row in cur:
    print(row)

cur.close()
conn.close()

"""Необходимо реализовать консольную программу с функциональностью телефонного справочника.
В консоли программа принимает следующие команды:
Добавить +79058023741 Бородин А.М.
Добавить 02 Полиция
Добавить 04 Служба газа
Эта команда добавляет в справочник соответствующее телефону ФИО. Телефон не содержит пробелов.
Найти 02
Найти Служба газа
Найти газ
Эта команда выводит всех абонентов, номер телефона или имя которых содержит приведённый текст.
Удалить 02
Удалить Бородин А.М.
Эта команда удаляет запись, телефон или название которой строго соответствует аргументу.
Выход
Эта команда сообщает системе что нужно прекратить принимать команды и завершить выполнение приложения.
При реализации этой программы необходимо создать
1. Интерфейс или абстрактный класс команды ICommand. Класс команды содержит один метод: выполнить команду, в качестве аргументов принимает строку, которая вызвала выполнение команды
2. Фасадный класс цикла обработки команд CommandLoop который содержит единственный публичный метод DoLoop(), который выполняется до тех пор, пока не будет вызвана команда Выход. Содержит внутри себя экземпляры классов фабрики команд и списка телефонов (List<класс данных>).
3. Класс данных который содержит два строковых поля: номер телефона и название абонента
4. Фабрику команд CommandFactory, которая принимает строку для выполнения и объект CommandLoop, а возвращает объект команды. Фабрика читает первую часть строки и выбирает конкретную реализацию команды. Команды могут обратиться к CommandLoop для перечитывания списка телефонов или сообщений циклу о том, что чтение команд необходимо прекратить и завершить DoLoop().
5. 4 класс реализующих команды Добавить, Найти, Удалить и Выход."""
