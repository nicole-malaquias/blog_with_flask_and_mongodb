from pymongo import MongoClient

client = MongoClient("localhost",27017)

# print(client.list_database_names()) vendo quais bds temos 


db = client.Kenzie


# db.create_collection('posts')
