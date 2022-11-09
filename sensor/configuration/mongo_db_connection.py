'''
Code for connection with MongoDB
'''

import pymongo
import os
import certifi
from sensor.constant.env_variable import MONGODB_URL_KEY
from sensor.constant.database import DATABASE_NAME
ca = certifi.where()
class MongoDBClient:
    client = None

    def __init__(self,database_name=DATABASE_NAME)->None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url="mongodb+srv://ansarialtaf23:AltAnsMohd@cluster0.7t5r1vg.mongodb.net/?retryWrites=true&w=majority"         # os.getenv(MONGODB_URL_KEY)
                print(mongo_db_url)

                if "localhost" in mongo_db_url:
                    MongoDBClient.client= pymongo.MongoClient(mongo_db_url)
                else:
                    MongoDBClient.client= pymongo.MongoClient(mongo_db_url,tlsCAFile=ca)

            self.client =MongoDBClient.client
            self.database=self.client[database_name]
            self.database_name = database_name

    
        except Exception as e:
            raise e