import sys
import logging

def errorMessageDetail(error: Exception, error_detail: sys):
    '''Extracts detailed error including file name, line number and error message
    Parameters:
    error: error that occured
    error_detail: the sys module to access traceback calls

    Outputs:
    error_message: A formatted error message string
    '''

    _, _, exc_tb = error_detail.exc_info()
    
    file_name = exc_tb.tb_frame.f_code.co_filename

    line_number = exc_tb.tb_lineno
    
    error_message = f'Error occured in python script: [{file_name}] at line number [{line_number}]: {str(error)}'

    logging.error(error_message)

    return error_message

class MyException(Exception):
    '''Custom exception class to handle errors in the Vehicle insurance application'''

    def __init__(self, error_message: str, error_detail: sys):
        '''Initializes the VehicleInsuranceException with a detailed error message
        Parameters:
        error_message: a string describing the error
        error_detail: the sys module to access the traceback details
        '''

        super().__init__(error_message)

        self.error_message = errorMessageDetail(error_message, error_detail)


    def __str__(self):
        '''Returns the string representation of error'''
        return self.error_message

        
