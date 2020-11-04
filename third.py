from pymongo import MongoClient  
import pprint  
client = MongoClient()  
 
db = client.theja
   
emp = db.employees.find({"id":"1"}).skip(1);  

for a in emp:
	pprint.pprint(a) 