import logging

config = logging.basicConfig(level=logging.DEBUG)

logging.debug('this is a DEBUG message ')
logging.info('this is an INFO message')
logging.warning('this is a warning message')
logging.error('this is an error message')
logging.critical('this is a critical message')