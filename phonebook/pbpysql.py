#!/usr/bin/env python
#https://www.tutorialspoint.com/python/python_database_access.htm
#https://stackoverflow.com/questions/35684400/how-to-use-python-3-5-1-with-a-mysql-database

import pymysql

# Open database connection
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='toshi',
                     db='TESTDB')
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
