from socket import socket, AF_INET, SOCK_STREAM
from jim.utils import send_message, get_message
from client import create_presence, check_message, create_message


client = socket(AF_INET, SOCK_STREAM)

client.connect(('localhost', 7777))

presense = create_presence()
send_message(client, presense)
response = check_message(get_message(client))
print(response)

while True:
    message = input('Введите сообщение, \'q\' закрытие клиента: ')
    if message == 'q':
        print('Программа завершена!')
        quit()
    msg = create_message(message)
    send_message(client, msg)



