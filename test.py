from pymongo import MongoClient

client = MongoClient('mongodb+srv://sparta:sparta313@cluster0.44y0f.mongodb.net/Cluster0?retryWrites=true&w=majority')

db = client.dbsnow

doc = {
        'id': "master",
        'name': "master",
        'key1': "master",
    }
print(doc)
db.users.insert_one(doc)