def download_data():
    print("FIle downloaded")

def extract_data():
    print("File extracted")

import logging
from datetime import datetime

log_file_name = datetime.now().strftime("log_%Y_%m_%d_%H_%M_%S.log")
logging.basicConfig(filename='t.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

def loggin_decorator(func):
    def wrapper(*args, **kwargs):
        logging.info("Function started")
        func(*args, **kwargs)
        logging.info("Function finished")
    return wrapper