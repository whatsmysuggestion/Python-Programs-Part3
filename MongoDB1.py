import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['niharika']

dblist = myclient.list_database_names()

print(dblist)