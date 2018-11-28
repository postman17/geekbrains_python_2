import sys
import time
from socket import socket, AF_INET, SOCK_STREAM
from jim.utils import send_message, get_message
from errors import UsernameLenError, MandatoryKeyError, ResponseCodeLenError, ResponseCodeError
from jim.settings import *

# Скрипт клиента месенджера
# флаги запуска:
# -a <address> - ip-адрес для прослушивания
# -p <port> - TCP-порт для работы сервера

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
    if flag == '-p':
        index = sys.argv.index(flag)
        try:
            temp_port = sys.argv[index + 1]
            port_flag = True
        except Exception:
            print('Введите порт после флага \'-p\'')
        try:
            port = int(temp_port)
        except:
            print('Порт должен быть целым числом!')
else:
    if not address_flag:
        address = 'localhost'
    elif not port_flag:
        port = 7777


def create_presence(account_name='Guest'):
    if not isinstance(account_name, str):
        raise TypeError
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


def check_message(response):
    if not isinstance(response, dict):
        raise TypeError
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
    client.connect((address, port))
    presence = create_presence()
    send_message(client, presence)
    response = get_message(client)
    response = check_message(response)
    print(response)
