from pymongo import MongoClient  

client = MongoClient(port=27017, host="localhost") 
 
db = client.theja
   
emp =db.employees.update_one({"id":"1"},{"$set":{'name':'testing'}}); 