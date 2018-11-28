from .settings import *
import json


def encode_to_bytes(request):
    if isinstance(request, dict):
        json_message = json.dumps(request)
        message = json_message.encode(ENCODING)
        return message
    else:
        raise TypeError


def decode_to_dict(response):
    if isinstance(response, bytes):
        enc_message = response.decode(ENCODING)
        message = json.loads(enc_message)
        if isinstance(message, dict):
            return message
        else:
            TypeError
    else:
        raise TypeError


def send_message(arg, message):
    bytes_message = encode_to_bytes(message)
    arg.send(bytes_message)


def get_message(arg):
    bytes_response = arg.recv(1024)
    response = decode_to_dict(bytes_response)
    return response
