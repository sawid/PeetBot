import pymongo

client = pymongo.MongoClient("mongodb+srv://peetbot:QxZ6cPBdL4jZ7wBo@cluster0.tabio.mongodb.net")

db = client["botdatabase"]

col = db["wordcollection"]

def addSentence (word, author):
    mydict = { "userId": author, "word": word }
    col.insert_one(mydict)