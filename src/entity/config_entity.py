import os
from src.constants import *
from dataclasses import dataclass
from datetime import datetime

TIMESTAMP = datetime.now().strftime('%d-%m-%y_%H:%M:%S')

@dataclass
class TrainingPipelineConfig:

    '''This class is used to create the training pipeline configuration.
    It creates the artifact directory and the pipeline name.'''

    pipeline_name = PIPELINE_NAME
    artifact_dir = os.path.join(ARTIFACT_DIR, TIMESTAMP)


training_pipeline_config = TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:

    '''This class is used to create the data ingestion configuration.
    It creates the data ingestion directory, feature store directory,
    ingested directory, and the training and testing file paths.'''

    data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir, DATA_INGESTION_DIR)
    feature_store_filepath = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR, DATA_FILENAME)
    training_filepath = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TRAIN_FILENAME)
    testing_filepath = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TEST_FILENAME)
    train_test_split_ratio = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    collection_name = COLLECTION_NAME

@dataclass
class DataValidationConfig:

    '''This class is used to create the data validation configuration.
    It creates the data validation directory, schema file path,
    and validation report file path.'''

    data_validation_dir = os.path.join(training_pipeline_config.artifact_dir, DATA_VALIDATION_DIR)
    validation_report_filepath = os.path.join(data_validation_dir, DATA_VALIDATION_REPORT_FILENAME)

@dataclass
class DataTransformationConfig:

    '''This class is used to create the data transformation configuration.
    It creates the data transformation directory, transformed data directory,
    transformed object directory, and the training and testing file paths.'''

    data_transformation_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_TRANSFORMATION_DIR)
    transformed_train_filepath: str = os.path.join(data_transformation_dir, DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
                                                    TRAIN_FILENAME.replace("csv", "npy"))
    transformed_test_filepath: str = os.path.join(data_transformation_dir, DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
                                                    TEST_FILENAME.replace("csv", "npy"))
    transformed_object_filepath: str = os.path.join(data_transformation_dir,
                                                    DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
                                                    PREPROCESSING_OBJECT_FILENAME)
    
@dataclass
class ModelTrainerConfig:
    model_trainer_dir = os.path.join(training_pipeline_config.artifact_dir, MODEL_TRAINER_DIR)
    trained_model_filepath = os.path.join(model_trainer_dir, MODEL_TRAINER_TRAINED_MODEL_DIR, MODEL_FILENAME)
    expected_accuracy = MODEL_TRAINER_EXPECTED_SCORE
    model_config_filepath = MODEL_TRAINER_MODEL_CONFIG_FILEPATH
    _n_estimators = MODEL_TRAINER_N_ESTIMATORS
    _min_samples_split = MODEL_TRAINER_MIN_SAMPLES_SPLIT
    _min_samples_leaf = MODEL_TRAINER_MIN_SAMPLES_LEAF
    _max_depth = MIN_SAMPLES_SPLIT_MAX_DEPTH
    _criterion = MIN_SAMPLES_SPLIT_CRITERION
    _random_state = MIN_SAMPLES_SPLIT_RANDOM_STATE

@dataclass
class ModelEvaluationConfig:
    '''This class is used to create the model evaluation configuration.'''

    changed_threshold_score: float = MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE
    bucket_name: str = MODEL_BUCKET_NAME
    s3_model_key_path: str = MODEL_FILENAME

@dataclass
class ModelPusherConfig:
    '''This class is used to create the model pusher configuration.'''

    bucket_name: str = MODEL_BUCKET_NAME
    s3_model_key_path: str = MODEL_FILENAME

@dataclass
class VehiclePredictorConfig:
    '''This class is used to create the vehicle predictor configuration.'''

    model_file_path: str = MODEL_FILENAME
    model_bucket_name: str = MODEL_BUCKET_NAME