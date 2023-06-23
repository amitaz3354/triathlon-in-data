import certifi as certifi
from pymongo import MongoClient


mongo_client = MongoClient(
            "mongodb+srv://amit_az3354:jkCAlLq7rFJ3VkTw@cluster0.somhr.mongodb.net/",
            tlsCAFile=certifi.where(),
            socketTimeoutMS=5000,
        )


db = mongo_client['TID']
collection = db['athletes-racing-history']


def import_athlete(doc):
    collection.insert_one(doc)