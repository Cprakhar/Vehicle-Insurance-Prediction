import json
import sys
import os

import pandas as pd

from pandas import DataFrame

from src.exception import MyException
from src.logger import logging
from src.utils.main_utils import read_yaml_file
from src.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from src.entity.config_entity import DataValidationConfig
from src.constants import SCHEMA_FILEPATH


class DataValidation:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifact, data_validation_config: DataValidationConfig):

        '''
        Parameters:
        ----------
        data_ingestion_artifact: DataIngestionArtifact
            Artifact for data ingestion
        data_validation_config: DataValidationConfig
            Configuration for data validation
        '''

        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config =read_yaml_file(filepath=SCHEMA_FILEPATH)
        except Exception as err:
            raise MyException(err, sys) from err

    def validate_number_of_columns(self, dataframe: DataFrame) -> bool:
        
        '''
        Method Name :   validate_number_of_columns
        Description :   This method validates the number of columns in the dataframe
        Output      :   Returns bool value based on validation results'''

        try:
            status = len(dataframe.columns) == len(self._schema_config["columns"])
            logging.info(f"Is required column present: [{status}]")
            return status
        except Exception as err:
            raise MyException(err, sys) from err

    def is_column_exist(self, df: DataFrame) -> bool:
        
        '''
        Method Name :   is_column_exist
        Description :   This method checks if the required columns exist in the dataframe
        Output      :   Returns bool value based on validation results'''


        try:
            dataframe_columns = df.columns
            missing_numerical_columns = []
            missing_categorical_columns = []
            for column in self._schema_config["numerical_columns"]:
                if column not in dataframe_columns:
                    missing_numerical_columns.append(column)

            if len(missing_numerical_columns)>0:
                logging.info(f"Missing numerical column: {missing_numerical_columns}")


            for column in self._schema_config["categorical_columns"]:
                if column not in dataframe_columns:
                    missing_categorical_columns.append(column)

            if len(missing_categorical_columns)>0:
                logging.info(f"Missing categorical column: {missing_categorical_columns}")

            return False if len(missing_categorical_columns)>0 or len(missing_numerical_columns)>0 else True
        except Exception as err:
            raise MyException(err, sys) from err

    @staticmethod
    def read_data(file_path) -> DataFrame:

        '''
        Method Name :   read_data
        Description :   This method reads the data from the given file path
        Output      :   Returns the dataframe'''

        try:
            return pd.read_csv(file_path)
        except Exception as err:
            raise MyException(err, sys)
        

    def initiate_data_validation(self) -> DataValidationArtifact:
        
        '''
        Method Name :   initiate_data_validation
        Description :   This method initiates the data validation process
        Output      :   Returns DataValidationArtifact object containing validation status and message'''

        try:
            validation_error_msg = ""
            logging.info("Starting data validation")
            train_df, test_df = (DataValidation.read_data(file_path=self.data_ingestion_artifact.training_filepath),
                                 DataValidation.read_data(file_path=self.data_ingestion_artifact.testing_filepath))

            # Checking col len of dataframe for train/test df
            status = self.validate_number_of_columns(dataframe=train_df)
            if not status:
                validation_error_msg += f"Columns are missing in training dataframe. "
            else:
                logging.info(f"All required columns present in training dataframe: {status}")

            status = self.validate_number_of_columns(dataframe=test_df)
            if not status:
                validation_error_msg += f"Columns are missing in test dataframe. "
            else:
                logging.info(f"All required columns present in testing dataframe: {status}")

            # Validating col dtype for train/test df
            status = self.is_column_exist(df=train_df)
            if not status:
                validation_error_msg += f"Columns are missing in training dataframe. "
            else:
                logging.info(f"All categorical/int columns present in training dataframe: {status}")

            status = self.is_column_exist(df=test_df)
            if not status:
                validation_error_msg += f"Columns are missing in test dataframe."
            else:
                logging.info(f"All categorical/int columns present in testing dataframe: {status}")

            validation_status = len(validation_error_msg) == 0

            data_validation_artifact = DataValidationArtifact(
                validation_status=validation_status,
                message=validation_error_msg,
                validation_report_filepath=self.data_validation_config.validation_report_filepath
            )

            # Ensure the directory for validation_report_file_path exists
            report_dir = os.path.dirname(self.data_validation_config.validation_report_filepath)
            os.makedirs(report_dir, exist_ok=True)

            # Save validation status and message to a JSON file
            validation_report = {
                "validation_status": validation_status,
                "message": validation_error_msg.strip()
            }

            with open(self.data_validation_config.validation_report_filepath, "w") as report_file:
                json.dump(validation_report, report_file, indent=4)

            logging.info("Data validation artifact created and saved to JSON file.")
            logging.info(f"Data validation artifact: {data_validation_artifact}")
            return data_validation_artifact
        except Exception as err:
            raise MyException(err, sys) from err