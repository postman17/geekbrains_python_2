import sys
from socket import socket, AF_INET, SOCK_STREAM
from jim.utils import send_message, get_message, decode_to_dict, encode_to_bytes
import log.server_log_config
import logging
from log.decorators import Log
import select

# Скрипт сервера месенджера
# флаги запуска:
# -a <address> - ip-адрес для прослушивания
# -p <port> - TCP-порт для работы сервера

# Функции логирования
logger = logging.getLogger('server-log')
log = Log(logger)


def log_info(message):
    logger.info(message)


def log_warning(message):
    logger.warning(message)


# Чтение флагов
address_flag = False
port_flag = False

for flag in sys.argv:
    if len(sys.argv) == 1:
        address = ''
        port = 7777
        break
    if flag == '-a':
        index = sys.argv.index(flag)
        try:
            address = sys.argv[index + 1]
            address_flag = True
        except Exception:
            log_warning('Попытка запуска скрипта сервера без введенного адреса после флага \'-а\'')
            print('Введите адрес после флага \'-а\'')
            quit()
    if flag == '-p':
        index = sys.argv.index(flag)
        try:
            temp_port = sys.argv[index + 1]
            port_flag = True
        except Exception:
            log_warning('Попытка запуска скрипта сервера без введенного порта после флага \'-p\'')
            print('Введите порт после флага \'-p\'')
            quit()
        try:
            port = int(temp_port)
        except Exception:
            log_warning('Попытка запуска скрипта сервера с нечисловым портом')
            print('Порт должен быть целым числом!')
            quit()
else:
    if not address_flag:
        address = ''
    elif not port_flag:
        port = 7777


@log
def presence_response(message):
    if 'action' in message and message['action'] == 'presence' and 'time' in message and isinstance(message['time'], float):
        return {'response': 200}
    else:
        return {'response': 400, 'error': 'Не верный запрос!'}


def check_message(message):
    if 'action' in message and message['action'] == 'msg' and 'time' in message and isinstance(message['time'], float):
        return True
    else:
        return False


def list_messages(clients):
    messages = []
    for client in clients:
        try:
            bytes_response = client.recv(1024)
            response = decode_to_dict(bytes_response)
            if check_message(response):
                messages.append(response)
            else:
                print('Неправильное сообщение!!!')
        except:
            pass
    return messages


if __name__ == '__main__':
    # Запуск сервера
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((address, port))
    server.listen(5)
    server.settimeout(0.2)
    log_info('Сервер запущен c адресом прослушивания: {}, на порту: {}'.format('ALL' if address == '' else address, port))
    print('Сервер запущен c адресом прослушивания: ', 'ALL' if address == '' else address, ' на порту: ', port)

    # Чтение и отправка запросов
    clients = []
    while True:
        try:
            cli, addr = server.accept()
            presence = get_message(cli)
            log_info(f'Получен запрос от клиента, с адреса: {addr[0]}')
            print('Получен запрос от клиента, с адреса: ', addr[0])
            response = presence_response(presence)
            send_message(cli, response)
            log_info(f'Отправлено presense сообщение на адрес: {addr[0]}')
        except OSError:
            pass
        else:
            print('Получен запрос на соединение от адреса:', addr)
            clients.append(cli)
        read = []
        write = []
        try:
            read, write, error = select.select(clients, clients, [], 0)
        except Exception:
            pass

        lst_msg = list_messages(read)
        for client in write:
            for msg in lst_msg:
                enc_msg = encode_to_bytes(msg)
                try:
                    client.send(enc_msg)
                except Exception:
                    clients.remove(client)
