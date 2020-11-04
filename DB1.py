#!/usr/bin/env python
import pymysql
#127.0.0.1   or local ipaddress or localhost
conn = pymysql.connect(host='localhost', port=3306, user='root', 
passwd='root',db='pavithra')


cursor = conn.cursor()


cursor.execute("SELECT VERSION()")


data = cursor.fetchone()
print ("Database version : %s " % data)


conn.close()