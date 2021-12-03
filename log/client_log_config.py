import logging
import logging.handlers

LOG = logging.getLogger('client')

FORMATTER = logging.Formatter('%(asctime)s - %(levelname)s -%(module)s - %(message)s')

FILE_HANDLER = logging.FileHandler("client.log", encoding='utf-8')
FILE_HANDLER.setLevel(logging.DEBUG)
FILE_HANDLER.setFormatter(FORMATTER)
LOG.addHandler(FILE_HANDLER)
LOG.setLevel(logging.DEBUG)

if __name__ == '__main__':
    LOG.critical('Критическая ошибка')
    LOG.error('Ошибка')
    LOG.debug('Отладочная информация')
    LOG.info('Информационное сообщение')