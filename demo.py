# from src.logger import logging

# logging.debug('This is demo logger-4')


# from src.exception import MyException
# import sys

# try:
#     a = 1 + 'Z'
# except Exception as err:
#     logging.info(err)
#     raise MyException(err, sys) from err

from src.pipeline.training_pipeline import TrainingPipeline

pipeline = TrainingPipeline()
pipeline.run_pipeline()