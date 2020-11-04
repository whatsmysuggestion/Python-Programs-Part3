from pymongo import MongoClient  
import pprint  
client = MongoClient()  
 
db = client.viral
   
emp = db.employees.find({});  

for a in emp:
	pprint.pprint(a) 