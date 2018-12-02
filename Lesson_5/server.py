import sys
from socket import socket, AF_INET, SOCK_STREAM
from jim.utils import send_message, get_message

# Скрипт сервера месенджера
# флаги запуска:
# -a <address> - ip-адрес для прослушивания
# -p <port> - TCP-порт для работы сервера

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
        address = ''
    elif not port_flag:
        port = 7777


def presence_response(message):
    if 'action' in message and message['action'] == 'presence' and 'time' in message and isinstance(message['time'], float):
        return {'response': 200}
    else:
        return {'response': 400, 'error': 'Не верный запрос!'}


if __name__ == '__main__':
    # Запуск сервера
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((address, port))
    server.listen(5)
    print('Сервер запущен c адресом прослушивания: ', 'ALL' if address == '' else address, ' на порту: ', port)

    # Чтение запросов
    while True:
        client, addr = server.accept()
        presence = get_message(client)
        print('Получен запрос от клиента, с адреса: ', addr[0])
        print(presence)
        response = presence_response(presence)
        send_message(client, response)
        client.close()
