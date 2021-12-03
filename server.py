# Программа-сервер
import logging
import socket
import sys
import json
from common.variables import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, \
    PRESENCE, TIME, USER, ERROR, DEFAULT_PORT, RESPONDEFAULT_IP_ADDRESSSE
from common.utils import get_message, send_message
from socket import SOL_SOCKET,SO_REUSEADDR

SERVER_LOGGER = logging.getLogger('server')

class Server:
    def client_message_handler(self,message):
        if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
                and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
            return {RESPONSE: 200}
        return {
            RESPONDEFAULT_IP_ADDRESSSE: 400,
            ERROR: 'Bad Request'
        }

def server_port():
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = DEFAULT_PORT
        if listen_port < 1024 or listen_port > 65535:
            SERVER_LOGGER.critical(
                f'Неверный номер порта:{server_port}.В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        SERVER_LOGGER.info(f'Получен серверный порт.')
        return listen_port


    except ValueError:
        SERVER_LOGGER.critical(
            'В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')
        # sys.exit(1)

def server_adress():
    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = ''
        SERVER_LOGGER.info(f'Получен серверный адрес. Если не указан,принимаются соединения с любых адресов.')
        return listen_address
    except ValueError:
        SERVER_LOGGER.critical('В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')


def main():
    server = Server()
    '''
    Загрузка параметров командной строки, если нет параметров, то задаём значения по умоланию.
    Сначала обрабатываем порт:
    server.py -p 8888 -a 127.0.0.1
    :return:
    '''
    # Готовим сокет

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.bind((server_adress(), server_port()))
    transport.setsockopt(SOL_SOCKET,SO_REUSEADDR, 5)

    # Слушаем порт

    transport.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = transport.accept()
        SERVER_LOGGER.info(f'Установлено соедение с ПК {client_address}')
        try:
            message_from_client = get_message(client)
            SERVER_LOGGER.debug(f'Получено сообщение от клиента: {message_from_client}')
            response = server.client_message_handler(message_from_client)
            send_message(client, response)
            SERVER_LOGGER.info(f' Отправление ответа клиенту {response}')
            SERVER_LOGGER.debug(f'Соединение с клиентом {client_address} закрывается.')
            client.close()
        except json.JSONDecodeError:
            SERVER_LOGGER.error(f'Не удалось декодировать сообщение, полученную от '
                                f'клиента {client_address}. Соединение закрывается.')
            client.close()
        except ValueError:
            SERVER_LOGGER.error(f'От клиента {client_address} приняты некорректные данные. '
                                f'Соединение закрывается.')
            client.close()


if __name__ == '__main__':
    main()

