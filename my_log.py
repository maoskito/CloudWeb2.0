#-*- coding: UTF-8 -*-
import logging
import sys
from logging.handlers import RotatingFileHandler


__all__ = ['logger', 'ERROR', 'DEBUG']

ERROR = logging.ERROR
DEBUG = logging.DEBUG

def get_logger(name='debug'):
    logger = logging.getLogger(name)
    fmt = logging.Formatter('%(asctime)s :[%(levelname)s]%(message)s')
    file_handler = RotatingFileHandler(name+'.log', mode='w', maxBytes=0)  # maxBytes=10*1024*1024
    print_handler = logging.StreamHandler(sys.stdout)

    file_handler.setFormatter(fmt)
    print_handler.setFormatter(fmt)

    logger.addHandler(file_handler)
    logger.addHandler(print_handler)

    logger.setLevel(1)
    return logger

# class Mylogger(object):
#     def __init__(self, name='debug'):
#         self.logger = get_logger(name)
#
#     def log(self, message):
#         self.logger.log(1, message)

logger = get_logger(name='debug')
case_logger = get_logger(name='case_log')

if __name__ == '__main__':
    pass


