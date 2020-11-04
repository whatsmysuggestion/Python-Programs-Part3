

import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', 
db='pavithra')
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql = """CREATE TABLE EMPLOYEE (
   FIRST_NAME  CHAR(20) NOT NULL,
   LAST_NAME  CHAR(20),
   AGE INT,  
   SEX CHAR(1),
   INCOME FLOAT )"""

cursor.execute(sql)

db.close()