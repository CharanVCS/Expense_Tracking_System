import logging
import os, sys

def setup_logging(name='log_helper',log_file='server.log' , level=logging.DEBUG):
    
    log_dir = os.path.dirname(__file__)
    sys.path.insert(0, log_dir)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
    
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

if __name__=='__main__':
    log_dir = os.path.dirname(__file__)
    print(log_dir)
    print(sys.path)