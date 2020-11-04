import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='demo')
cursor = conn.cursor()

sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
   LAST_NAME, AGE, SEX, INCOME)
   VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:

   cursor.execute(sql)

   conn.commit()
except:

    conn.rollback()


conn.close()