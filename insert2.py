
import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', 
passwd='root', db='adv')
cursor = conn.cursor()

name=input("enter a name")
lname=input("enter last name")
age=int(input("enter a age"))
s=input("enter sex")
income=int(input("enter income"))

sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
   LAST_NAME, AGE, SEX, INCOME) \
   VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
   (name, lname, age, s, income)
try:
   cursor.execute(sql)
   conn.commit()
except:
    conn.rollback()
conn.close()