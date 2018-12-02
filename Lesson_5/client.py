import sys
import time
from socket import socket, AF_INET, SOCK_STREAM
from jim.utils import send_message, get_message
from errors import UsernameLenError, MandatoryKeyError, ResponseCodeLenError, ResponseCodeError
from jim.settings import *
import log.client_log_config
import logging

# Скрипт клиента месенджера
# флаги запуска:
# -a <address> - ip-адрес для прослушивания
# -p <port> - TCP-порт для работы сервера

# Функции логирования
logger = logging.getLogger('client-log')


def log_info(message):
    logger.info(message)


def log_warning(message):
    logger.warning(message)


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


def create_presence(account_name='Guest'):
    if not isinstance(account_name, str):
        log_warning('Формирование presense сообщения. Account_name не является строкой.')
        raise TypeError
    if len(account_name) > 25:
        log_warning('Формирование presense сообщения. Длина account_name больше 25 символов.')
        raise UsernameLenError(account_name)
    message = {
        'action': 'presence',
        'time': time.time(),
        'user': {
            'account_name': account_name
        }
    }
    log_info('Сформировано presense сообщение.')
    return message


def check_message(response):
    if not isinstance(response, dict):
        log_warning('Проверка полученного сообщения. Сообщение не является словарем.')
        raise TypeError
    if 'response' not in response:
        log_warning('Проверка полученного сообщения. В сообщении отсутствует поле \'response\'.')
        raise MandatoryKeyError('response')
    code = response['response']
    if len(str(code)) != 3:
        log_warning('Проверка полученного сообщения. Неправильная длина кода ответа сервера.')
        raise ResponseCodeLenError(code)
    if code not in RESPONSE_CODES:
        log_warning('Проверка полученного сообщения. Неправильный код ответа сервера.')
        raise ResponseCodeError(code)
    log_info('Полученное сообщение проверено.')
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
    log_info(f'Установлено подключение по адресу {address}, порт {port}')
    presence = create_presence()
    send_message(client, presence)
    log_info('Отправлено presense сообщение')
    response = get_message(client)
    log_info('Получен ответ на presense сообщение')
    response = check_message(response)
    print(response)
