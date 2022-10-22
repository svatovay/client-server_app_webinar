import sys
import json
from socket import socket, AF_INET, SOCK_STREAM
import time
import logging

from common.decos import Log
from logs.config import client_log_config

from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, \
    RESPONSE, ERROR, DEFAULT_IP_ADDRESS, DEFAULT_PORT
from common.utils import get_message, send_message

# Инициализация логирования сервера.
logger = logging.getLogger('client_dist')


@Log(logger)
def create_presence(account_name='Guest'):
    '''
    Функция генерирует запрос о присутствии клиента
    :param account_name:
    :return:
    '''
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return out


@Log(logger)
def process_ans(message):
    '''
    Функция разбирает ответ сервера
    :param message:
    :return:
    '''
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError


@Log(logger)
def main():
    '''Загружаем параметы коммандной строки'''
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        logger.info(f'SERVER ADDRESS: {server_address}, SERVER PORT: {server_port},')
        if not (1024 < server_port < 65535):
            logger.critical(
                f'Попытка запуска клиента с неподходящим номером порта: {server_port}. '
                f'В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
            sys.exit(1)
    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT

    # Инициализация сокета и обмен

    transport = socket(AF_INET, SOCK_STREAM)
    transport.connect((server_address, server_port))
    message_to_server = create_presence()
    send_message(transport, message_to_server)
    try:
        answer = process_ans(get_message(transport))
        logger.info(f'SERVER ANSWER: {answer}')
    except (ValueError, json.JSONDecodeError):
        logger.critical(f'Не удалось декодировать сообщение сервера: {answer}.')


if __name__ == '__main__':
    main()
