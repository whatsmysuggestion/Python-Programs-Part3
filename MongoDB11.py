import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["akash"]
mycol = mydb["customers"]

myresult = mycol.find().limit(5)


for x in myresult:
  print(x)
