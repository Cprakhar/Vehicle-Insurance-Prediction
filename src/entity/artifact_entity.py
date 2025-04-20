from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:

    '''This class is used to create the data ingestion artifact.'''

    training_filepath: str
    testing_filepath: str

@dataclass
class DataValidationArtifact:
    
    '''This class is used to create the data validation artifact.'''

    validation_status:bool
    message: str
    validation_report_filepath: str