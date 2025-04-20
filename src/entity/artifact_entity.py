from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    '''This class is used to create the data ingestion artifact.'''

    training_filepath: str
    testing_filepath: str

@dataclass
class DataValidationArtifact:
    '''This class is used to create the data validation artifact.'''

    validation_status: bool
    message: str
    validation_report_filepath: str


@dataclass
class DataTransformationArtifact:
    '''This class is used to create the data transformation artifact.'''

    transformed_object_filepath: str 
    transformed_train_filepath: str
    transformed_test_filepath: str

@dataclass
class ClassificationMetricArtifact:
    '''This class is used to create the classification metric artifact.'''

    accuracy_score:float
    f1_score:float
    precision_score:float
    recall_score:float

@dataclass
class ModelTrainerArtifact:
    '''This class is used to create the model trainer artifact.'''

    trained_model_filepath:str 
    metric_artifact:ClassificationMetricArtifact

@dataclass
class ModelEvaluationArtifact:
    '''This class is used to create the model evaluation artifact.'''

    is_model_accepted:bool
    changed_accuracy:float
    s3_model_path:str 
    trained_model_path:str

@dataclass
class ModelPusherArtifact:
    '''This class is used to create the model pusher artifact.'''

    bucket_name:str
    s3_model_path:str