from socket import socket, AF_INET, SOCK_STREAM
from jim.utils import send_message, get_message
from client import create_presence, check_message, read_message


client = socket(AF_INET, SOCK_STREAM)


client.connect(('localhost', 7777))

presense = create_presence()
send_message(client, presense)
response = check_message(get_message(client))
print(response)
while True:
    response = read_message(get_message(client))
    print(response)
