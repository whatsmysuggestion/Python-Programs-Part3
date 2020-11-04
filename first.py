from pymongo import MongoClient  
import pprint  

client = MongoClient()   # local machine  local mongodb 27017
  
db = client.viral
  
employee = {"id": "1","name": "a","profession": "SE"}  
   
emp = db.employees  
 
emp.insert_one(employee)  
pprint.pprint(emp.find_one()) 
#pip install pymongo