import os
from datetime import date

DB_NAME = 'MLOps-database-1'
COLLECTION_NAME = 'Vehicle-collection'
DB_CONNECTION_STRING = 'DB_URL'

PIPELINE_NAME = ''
ARTIFACT_DIR = 'artifacts'

MODEL_FILENAME = 'model.pkl'

TARGET_COLUMN = 'Response'
CURRENT_YEAR = date.today().year

PREPROCESSING_OBJECT_FILENAME = 'preprocessing.pkl'

DATA_FILENAME = 'data.csv'
TRAIN_FILENAME = 'train.csv'
TEST_FILENAME = 'test.csv'
SCHEMA_FILEPATH = os.path.join('config', 'schema.yaml')

AWS_ACCESS_KEY_ENV_KEY = 'AWS_ACCESS_KEY'
AWS_SECRET_ACCESS_KEY_ENV_KEY = 'AWS_SECRET_ACCESS_KEY'
REGION_NAME = 'ap-south-1'



# Constants related to the data ingestion component
DATA_INGESTION_DIR = 'data_ingestion'
DATA_INGESTION_FEATURE_STORE_DIR = 'feature_store'
DATA_INGESTION_INGESTED_DIR = 'ingested'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO = 0.25


# Constants related to the data validation component
DATA_VALIDATION_DIR = 'data_validation'
DATA_VALIDATION_REPORT_FILENAME = 'report.yaml'

# Constants related to the data transformation component
DATA_TRANSFORMATION_DIR = 'data_transformation'
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR = 'transformed'
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR = 'transformed_object'


# Constants related to the model trainer component
MODEL_TRAINER_DIR = 'model_trainer'
MODEL_TRAINER_TRAINED_MODEL_DIR = 'trained_model'
MODEL_TRAINER_TRAINED_MODEL_NAME = 'model.pkl'
MODEL_TRAINER_EXPECTED_SCORE = 0.6
MODEL_TRAINER_MODEL_CONFIG_FILEPATH = os.path.join('config', 'model.yaml')
MODEL_TRAINER_N_ESTIMATORS = 200
MODEL_TRAINER_MIN_SAMPLES_SPLIT = 7
MODEL_TRAINER_MIN_SAMPLES_LEAF = 6
MIN_SAMPLES_SPLIT_MAX_DEPTH = 10
MIN_SAMPLES_SPLIT_CRITERION = 'entropy'
MIN_SAMPLES_SPLIT_RANDOM_STATE = 101


# Constants related to the model evaluation component
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE = 0.02
MODEL_BUCKET_NAME = "pchha-mlops-bucket"
MODEL_PUSHER_S3_KEY = "model-registry"


APP_HOST = "0.0.0.0"
APP_PORT = 5000