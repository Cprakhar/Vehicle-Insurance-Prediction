import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime

log_dir = 'logs'
log_file = f'{datetime.now().strftime('%d-%m-%Y_%H:%M:%S')}.log'
max_log_size = 5*1024*1042 # 5 MiB
backup_count = 3 # Number of backups to keep

log_dir_path = os.path.join(os.getcwd(), log_dir)
os.makedirs(log_dir_path, exist_ok=True)
log_file_path = os.path.join(log_dir_path, log_file)

def configLogger():

    '''Configures logging with rotating file handler and console handler'''

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s')

    fileHandler = RotatingFileHandler(log_file_path, maxBytes=max_log_size, backupCount=backup_count)
    fileHandler.setLevel(logging.DEBUG)
    fileHandler.setFormatter(formatter)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.DEBUG)
    consoleHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)
    logger.addHandler(consoleHandler)


configLogger()
