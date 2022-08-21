import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["botdatabase"]

col = db["wordcollection"]

def addSentence (word, author):
    mydict = { "userId": author, "word": word }
    x = col.insert_one(mydict)