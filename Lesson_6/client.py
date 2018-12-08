import sys
import time
from socket import socket, AF_INET, SOCK_STREAM
from jim.utils import send_message, get_message
from errors import UsernameLenError, MandatoryKeyError, ResponseCodeLenError, ResponseCodeError, AccountNameNotStr, ResponseNotDict
from jim.settings import *
import log.client_log_config
import logging
from log.decorators import Log

# Скрипт клиента месенджера
# флаги запуска:
# -a <address> - ip-адрес для прослушивания
# -p <port> - TCP-порт для работы сервера

# Функции логирования
logger = logging.getLogger('client-log')
log = Log(logger)


# def log_info(message):
#     logger.info(message)
#
#
# def log_warning(message):
#     logger.warning(message)


def log_critical(message):
    logger.critical(message)


# Чтение флагов
address_flag = False
port_flag = False

for flag in sys.argv:
    if len(sys.argv) == 1:
        address = 'localhost'
        port = 7777
        break
    if flag == '-a':
        index = sys.argv.index(flag)
        try:
            address = sys.argv[index + 1]
            address_flag = True
        except Exception:
            print('Введите адрес после флага \'-а\'')
            log_warning('Попытка запуска скрипта сервера без введенного адреса после флага \'-а\'')
            quit()
    if flag == '-p':
        index = sys.argv.index(flag)
        try:
            temp_port = sys.argv[index + 1]
            port_flag = True
        except Exception:
            print('Введите порт после флага \'-p\'')
            log_warning('Попытка запуска скрипта сервера без введенного порта после флага \'-p\'')
            quit()
        try:
            port = int(temp_port)
        except Exception:
            print('Порт должен быть целым числом!')
            log_warning('Попытка запуска скрипта сервера с нечисловым портом')
            quit()
else:
    if not address_flag:
        address = 'localhost'
    elif not port_flag:
        port = 7777


@log
def create_presence(account_name='Guest'):
    raise AccountNameNotStr(account_name)
    if not isinstance(account_name, str):
        raise AccountNameNotStr(account_name)

    if len(account_name) > 25:
        raise UsernameLenError(account_name)
    message = {
        'action': 'presence',
        'time': time.time(),
        'user': {
            'account_name': account_name
        }
    }
    return message


@log
def check_message(response):
    if not isinstance(response, dict):
        raise ResponseNotDict(response)
    if 'response' not in response:
        raise MandatoryKeyError('response')
    code = response['response']
    if len(str(code)) != 3:
        raise ResponseCodeLenError(code)
    if code not in RESPONSE_CODES:
        raise ResponseCodeError(code)
    return response


if __name__ == '__main__':
    # Создаем сокет
    client = socket(AF_INET, SOCK_STREAM)
    # Соединяемся с сервером
    try:
        client.connect((address, port))
    except ConnectionRefusedError:
        print('Соединение с сервером не установлено!')
        log_critical('Соединение с сервером не установлено!')
        quit()
    presence = create_presence()
    send_message(client, presence)
    response = get_message(client)
    response = check_message(response)
    print(response)
