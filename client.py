# Программа-клиент

import sys
import json
import socket
import time
import logging
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, \
    RESPONSE, ERROR, DEFAULT_IP_ADDRESS, DEFAULT_PORT
from common.utils import get_message, send_message
try:
    # python 3.4+ should use builtin unittest.mock not mock package
    from unittest.mock import patch
except ImportError:
    from mock import patch

CLIENT_LOGGER = logging.getLogger('client')

class Client():
    data_to_server = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: 'Guest'
        }
    }

    def check_response(self, message):
        CLIENT_LOGGER.debug(f'Разбор сообщения от сервера: {message}')
        if RESPONSE in message:
            if message[RESPONSE] == 200:
                return ('200 : OK')
            return (f'400 : {message[ERROR]}')
        raise ValueError

def check_port():
    try:
        # print(sys.argv)
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])

        if server_port < 1024 or server_port > 65535:
            CLIENT_LOGGER.critical(
                f'Неверный номер порта:{server_port}.В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        CLIENT_LOGGER.info(f'Клиент успешно запущен : адрес сервера: {server_address} , порт: {server_port}')
    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
        CLIENT_LOGGER.info(f'Клиент успешно запущен : адрес сервера: {server_address} , порт: {server_port}')
    return [server_address,server_port]

def main():
    print(CLIENT_LOGGER.level)
    try:
        client = Client()
        check_port()
        server_address, server_port = check_port()
        transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        transport.connect((server_address, server_port))
        message_to_server = client.data_to_server
        send_message(transport, message_to_server)
        answer = client.check_response(get_message(transport))
        CLIENT_LOGGER.info(f'Получен ответ от сервера: {answer}')
    except json.JSONDecodeError:
        CLIENT_LOGGER.error('Не удалось декодировать сообщение.')
    except ConnectionRefusedError:
        CLIENT_LOGGER.critical(f'Не удалось подключиться к серверу {server_address}:{server_port}, '
                               f'конечный компьютер отверг запрос на подключение.')
    except ValueError:
        CLIENT_LOGGER.error(f'Некорректный ответ сервера')


if __name__ == '__main__':
    main()