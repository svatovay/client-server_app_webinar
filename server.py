import json
import sys
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import logging
from logs.config import server_log_config

from common.variables import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, \
    PRESENCE, TIME, USER, ERROR, DEFAULT_PORT
from common.utils import get_message, send_message
from common.decos import Log

# Инициализация логирования сервера.
logger = logging.getLogger('server_dist')


@Log(logger)
def process_client_message(message):
    '''
    Обработчик сообщений от клиентов, принимает словарь -
    сообщение от клинта, проверяет корректность,
    возвращает словарь-ответ для клиента

    :param message:
    :return:
    '''
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
            and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


@Log(logger)
def main():
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = DEFAULT_PORT
        if not (1024 < listen_port < 65535):
            logger.critical(
                f'Попытка запуска клиента с неподходящим номером порта: {listen_port}. '
                f'Значение порта может быть в диапазоне от 1024 до 65535.')
            sys.exit(1)
    except IndexError:
        logger.error(
            f'Неверно указан параметр \"-p\".'
            f'После параметра \"-p\" необходимо указать номер порта.')
        sys.exit(1)

    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = ''
    except IndexError:
        logger.error(
            f'Неверно указан параметр \"-a\".'
            f'После параметра \"-a\" необходимо указать адрес, который будет слушаться сервером.')
        sys.exit(1)

    transport = socket(AF_INET, SOCK_STREAM)
    transport.bind((listen_address, listen_port))
    transport.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    transport.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = transport.accept()
        try:
            message_from_client = get_message(client)
            logger.info(f'CLIENT MESSAGE: {message_from_client}')
            response = process_client_message(message_from_client)
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            logger.critical('Принято некорректное сообщение от клиента')
            client.close()


if __name__ == '__main__':
    main()
