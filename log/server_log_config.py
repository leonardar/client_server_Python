import logging
import os
import sys
from logging import handlers
from common.variables import LOGGING_LEVEL
sys.path.append('../')

LOG = logging.getLogger('server')
FORMATTER = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(message)s')

PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'server.log')

FILE_HANDLER = handlers.TimedRotatingFileHandler(PATH, encoding='utf8', interval=1, when='D')
FILE_HANDLER.setLevel(logging.DEBUG)
FILE_HANDLER.setFormatter(FORMATTER)
LOG.addHandler(FILE_HANDLER)
LOG.setLevel(LOGGING_LEVEL)

if __name__ == '__main__':
    LOG.critical('Критическая ошибка')
    LOG.error('Ошибка')
    LOG.debug('Отладочная информация')
    LOG.info('Информационное сообщение')