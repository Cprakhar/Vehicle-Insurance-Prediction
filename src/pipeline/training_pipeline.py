import sys
from src.exception import MyException
from src.logger import logging

from src.components.data_ingestion import DataIngestion

from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact

class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info('Starting data ingestion...')
            logging.info('Getting data from mongoDB...')
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info('Data ingestion completed successfully.')
            logging.info('Exiting data ingestion...')
            return data_ingestion_artifact
        
        except Exception as err:
            raise MyException(err, sys) from err
        
    def run_pipeline(self) -> None:
        try:
            logging.info('Starting the training pipeline...')
            data_ingestion_artifact = self.start_data_ingestion()
            logging.info('Training pipeline completed successfully.')
        
        except Exception as err:
            raise MyException(err, sys) from err