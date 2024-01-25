from housing.logger import logging
import os
import sys
def get_error_message_detail(error_message,error_detail:sys)->str:
    _,_,exec_tb=error_detail.exc_info()
    try_block_line_number=exec_tb.tb_lineno
    exception_line_number=exec_tb.tb_frame.f_lineno
    file_name=exec_tb.tb_frame.f_code.co_filename
    
    error_message=f"Error occured in the script: {file_name} \n try block lineno: {try_block_line_number} \n exception line number: {exception_line_number} \n error message: {error_message}."
    logging.info(error_message)
    return error_message
    
    
class CustomException(Exception):
    def __init__(self,error_message:Exception,error_detail:sys):
        super().__init__(error_message)
        self.error_message=get_error_message_detail(error_message=error_message,error_detail=error_detail)
        
    def __str__(self):
        return self.error_message
    
    def __repr__(self):
        return CustomException.__name__.str()
    
    