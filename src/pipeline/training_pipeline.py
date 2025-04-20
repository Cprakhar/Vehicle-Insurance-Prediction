import sys
from src.exception import MyException
from src.logger import logging

from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation

from src.entity.config_entity import DataIngestionConfig, DataValidationConfig
from src.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact


class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:

        '''This method is used to ingest the data from the source. It fetches the data from the MongoDB database and saves it in the feature store.'''

        logging.info('Starting data ingestion...')
        try:
            logging.info('Getting data from mongoDB...')
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info('Data ingestion completed successfully.')
            logging.info('Exiting data ingestion...')
            return data_ingestion_artifact
        
        except Exception as err:
            raise MyException(err, sys) from err
        
    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:

        '''This method is used to validate the data. It checks if the data is in the correct format and if it meets the requirements.'''

        logging.info('Starting data validation...')
        try:
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,
                                             data_validation_config=self.data_validation_config)
            data_validation_artifact = data_validation.initiate_data_validation()
            logging.info('Data validation completed successfully.')
            logging.info('Exiting data validation...')
            return data_validation_artifact
        
        except Exception as err:
            raise MyException(err, sys) from err

    def run_pipeline(self) -> None:

        '''This method is used to run the entire pipeline. It calls all the methods in the correct order.'''

        logging.info('Starting the training pipeline...')
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            logging.info('Training pipeline completed successfully.')
        
        except Exception as err:
            raise MyException(err, sys) from err