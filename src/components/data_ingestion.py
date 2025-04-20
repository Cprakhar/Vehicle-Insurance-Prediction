import os
import sys

from pandas import DataFrame
from sklearn.model_selection import train_test_split

from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact
from src.exception import MyException
from src.logger import logging
from src.data_access.vehicle_data import VehicleData

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):

        '''
        Parameters:
        ----------
        data_ingestion_config: DataIngestionConfig
            Configuration for data ingestion
        '''

        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as err:
            raise MyException(err, sys) from err

    def export_data_into_feature_store(self) -> DataFrame:

        '''
        This method is used to export the data from the MongoDB database and save it into the feature store.
        It fetches the data from the MongoDB database and converts it into a pandas DataFrame.
        '''

        try:
            logging.info('Exporting data from mongoDB')
            vehicle_data = VehicleData()
            dataframe = vehicle_data.export_collection(collection_name=self.data_ingestion_config.collection_name)
            logging.info(f'Shape of the data: {dataframe.shape}')
            feature_store_filepath = self.data_ingestion_config.feature_store_filepath
            dir = os.path.dirname(feature_store_filepath)
            os.makedirs(dir, exist_ok=True)
            logging.info(f'Saving data into feature store at {feature_store_filepath}')

            dataframe.to_csv(feature_store_filepath, index=False, header=True)
            return dataframe
        except Exception as err:
            raise MyException(err, sys) from err
        
    def split_data_as_train_test(self, dataframe: DataFrame) -> None:


        '''
        This method is used to split the data into training and testing datasets.
        Parameters:
        ----------
        dataframe: DataFrame
            The dataframe to be split into train and test datasets.
        '''

        logging.info('Entered the split_data_as_train_test method of DataIngestion class')
        try:
            train_set, test_set = train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio, random_state=42)
            logging.info('Performed train test split on the dataframe')
            logging.info('Exited the split_data_as_train_test method of DataIngestion class')

            dir = os.path.dirname(self.data_ingestion_config.training_filepath)
            os.makedirs(dir, exist_ok=True)

            logging.info('Exporting train and test data to respective file paths')
            train_set.to_csv(self.data_ingestion_config.training_filepath, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.testing_filepath, index=False, header=True)
            logging.info('Exported train and test data to respective file paths')

        except Exception as err:
            raise MyException(err, sys) from err
        
    def initiate_data_ingestion(self) -> DataIngestionArtifact:

        '''
        This method is used to initiate the data ingestion process.
        It fetches the data from the MongoDB database and saves it in the feature store.
        It also splits the data into training and testing datasets.
        Returns:
        -------
        DataIngestionArtifact
            The artifact containing the file paths of the training and testing datasets.
        '''


        logging.info('Entered the initiate_data_ingestion method of DataIngestion class')

        try:
            dataframe = self.export_data_into_feature_store()
            logging.info('Got the data from mongoDB')
            self.split_data_as_train_test(dataframe=dataframe)
            logging.info('Performed train test split in the dataset')

            logging.info('Exited the initiate_data_ingestion method of DataIngestion class')

            data_ingestion_artifact = DataIngestionArtifact(training_filepath=self.data_ingestion_config.training_filepath, testing_filepath=self.data_ingestion_config.testing_filepath)
            logging.info(f'Data ingestion artifact: {data_ingestion_artifact}')
            return data_ingestion_artifact
         
        except Exception as err:
            raise MyException(err, sys) from err
