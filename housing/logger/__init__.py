import os
import sys 
import logging

from housing.constant import current_time_stamp

log_file_name=f"{current_time_stamp}.log"
logs_path=os.path.join(os.getcwd(),"logs")
os.makedirs(logs_path,exist_ok=True)
log_file_path=os.path.join(logs_path,log_file_name)

logging.basicConfig(filename=log_file_path,
                    filemode="w",
                    format="[%(asctime)s]-%(levelname)s-%(filename)s-%(lineno)d-%(message)s",
                    level=logging.INFO)

