import sys

def error_message_detail(error, error_message):
  _,_, exc_tb = sys.exc_info() #this give 3 placeholders first 2 are not that useful, 3rd is the traceback object  that helps us to get the line number of the error
  
  file_name = exc_tb.tb_frame.f_code.co_filename
  error_message = f'Error Occured in file: {file_name} at line number: {exc_tb.tb_lineno} with error message: {error_message}'
  
  return error_message


class CustomException(Exception):
  
  def __init__(self, error_message, error_detail:sys):
    super().__init__(error_message)
    self.error_message = error_message_detail(error_detail, error_message)
    
    
  def __str__(self):
    return self.error_message