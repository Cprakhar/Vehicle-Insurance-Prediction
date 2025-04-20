import os
import sys
import pymongo
import certifi

from src.exception import MyException
from src.logger import logging

from src.constants import DB_NAME, DB_CONNECTION_STRING

ca = certifi.where()

class MongoDBClient:

    '''This class is used to connect to the MongoDB database.'''
    
    client = None

    def __init__(self, database_name: str = DB_NAME) -> None :
        try:
            if MongoDBClient.client is None:
                db_url = os.getenv(DB_CONNECTION_STRING)

                if db_url is None:
                    raise Exception(f'Environment variable: {DB_CONNECTION_STRING} is not set')
            
                MongoDBClient.client = pymongo.MongoClient(db_url, tlsCAFile=ca)
            
            self.client = MongoDBClient.client
            self.database = self.client.get_database(DB_NAME)
            self.database_name = database_name

            logging.info('MongoDB connection successful')

        except Exception as err:
            raise MyException(err, sys)

        
