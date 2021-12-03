import logging
import sys
import os
import logging.handlers
sys.path.append('../')

LOG = logging.getLogger('client')
PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'client.log')

FORMATTER = logging.Formatter('%(asctime)s - %(levelname)s -%(module)s - %(message)s')

FILE_HANDLER = logging.FileHandler(PATH, encoding='utf-8')
FILE_HANDLER.setLevel(logging.DEBUG)
FILE_HANDLER.setFormatter(FORMATTER)
LOG.addHandler(FILE_HANDLER)
LOG.setLevel(logging.DEBUG)

if __name__ == '__main__':
    LOG.critical('Критическая ошибка')
    LOG.error('Ошибка')
    LOG.debug('Отладочная информация')
    LOG.info('Информационное сообщение')