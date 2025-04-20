from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    training_filepath: str
    testing_filepath: str