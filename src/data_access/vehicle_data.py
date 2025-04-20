import sys
import numpy as np
import pandas as pd
from typing import Optional

from src.configuration.mongodb_config import MongoDBClient
from src.constants import DB_NAME
from src.exception import MyException

class VehicleData:

    '''This class is used to fetch the data from the MongoDB database and convert it into a pandas DataFrame.'''

    def __init__(self) -> None:
        try:
            self.mongodb_client = MongoDBClient(database_name=DB_NAME)
        except Exception as err:
            raise MyException(err, sys)
        
    def export_collection(self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:

        '''This method is used to fetch the data from the MongoDB database and convert it into a pandas DataFrame.'''

        try:
            if database_name is None:
                collection = self.mongodb_client.database.get_collection(collection_name)
            else:
                collection = self.mongodb_client.client.get_database(database_name).get_collection(collection_name)

            print('Fetching data from mongoDB...')
            df = pd.DataFrame(list(collection.find()))
            print(f'Data located with len: {len(df)}')
            if '_id' in df.columns.to_list():
                df.drop(columns='_id', axis=1, inplace=True)
            df.replace({'na': np.nan}, inplace=True)
            return df
        
        except Exception as err:
            raise MyException(err, sys)