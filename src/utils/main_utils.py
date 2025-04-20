import os
import sys

import numpy as np
import dill
import yaml
from pandas import DataFrame

from src.exception import MyException
from src.logger import logging


def read_yaml_file(filepath: str) -> dict:
    try:
        with open(filepath, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as err:
        raise MyException(err, sys) from err


def write_yaml_file(filepath: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(filepath):
                os.remove(filepath)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w") as file:
            yaml.dump(content, file)
    except Exception as err:
        raise MyException(err, sys) from err


def load_object(filepath: str) -> object:
    """
    Returns model/object from project directory.
    filepath: str location of file to load
    return: Model/Obj
    """
    try:
        with open(filepath, "rb") as file_obj:
            obj = dill.load(file_obj)
        return obj
    except Exception as err:
        raise MyException(err, sys) from err

def save_numpy_array_data(filepath: str, array: np.array):
    """
    Save numpy array data to file
    filepath: str location of file to save
    array: np.array data to save
    """
    try:
        dir_path = os.path.dirname(filepath)
        os.makedirs(dir_path, exist_ok=True)
        with open(filepath, 'wb') as file_obj:
            np.save(file_obj, array)
    except Exception as err:
        raise MyException(err, sys) from err


def load_numpy_array_data(filepath: str) -> np.array:
    """
    load numpy array data from file
    filepath: str location of file to load
    return: np.array data loaded
    """
    try:
        with open(filepath, 'rb') as file_obj:
            return np.load(file_obj)
    except Exception as err:
        raise MyException(err, sys) from err


def save_object(filepath: str, obj: object) -> None:
    logging.info("Entered the save_object method of utils")

    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "wb") as file_obj:
            dill.dump(obj, file_obj)

        logging.info("Exited the save_object method of utils")

    except Exception as err:
        raise MyException(err, sys) from err


# def drop_columns(df: DataFrame, cols: list)-> DataFrame:

#     """
#     drop the columns form a pandas DataFrame
#     df: pandas DataFrame
#     cols: list of columns to be dropped
#     """
#     logging.info("Entered drop_columns methon of utils")

#     try:
#         df = df.drop(columns=cols, axis=1)

#         logging.info("Exited the drop_columns method of utils")
        
#         return df
#     except Exception as err:
#         raise MyException(err, sys) from err