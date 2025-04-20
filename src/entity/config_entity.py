import os
from src.constants import *
from dataclasses import dataclass
from datetime import datetime

TIMESTAMP = datetime.now().strftime('%d-%m-%y_%H:%M:%S')

@dataclass
class TrainingPipelineConfig:
    pipeline_name = PIPELINE_NAME
    artifact_dir = os.path.join(ARTIFACT_DIR, TIMESTAMP)


training_pipeline_config = TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:
    data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir, DATA_INGESTION_DIR)
    feature_store_filepath = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR, DATA_FILENAME)
    training_filepath = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TRAIN_FILENAME)
    testing_filepath = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TEST_FILENAME)
    train_test_split_ratio = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    collection_name = COLLECTION_NAME