import unittest
import socket
import json
from utils import encode_to_bytes, decode_to_dict, send_message, get_message


class TestEncodeDecodeToBytes(unittest.TestCase):

    def test_encode_with_not_dict(self):
        with self.assertRaises(TypeError):
            encode_to_bytes('Test messages')

    def test_encode_with_right_request(self):
        self.assertEqual(encode_to_bytes({'test': 'test'}), b'{"test": "test"}')

    def test_decode_with_response_not_bytes(self):
        with self.assertRaises(TypeError):
            decode_to_dict('Test messages')

    def test_decode_with_response_not_dict(self):
        with self.assertRaises(TypeError):
            decode_to_dict(b'["Test messages"]')

    def test_decode_with_right_response(self):
        self.assertEqual(decode_to_dict(b'{"test": "test"}'), {'test': 'test'})


class ClientSocket():

    def __init__(self, sock_type=socket.AF_INET, sock_family=socket.SOCK_STREAM):
        pass

    def recv(self, n):
        message = {'response': 200}
        jmassage = json.dumps(message)
        bmessage = jmassage.encode('utf-8')
        return bmessage

    def send(self, bmessage):
        pass


class TestGetSendMessage(unittest.TestCase):

    def test_get_message(self):
        sock = ClientSocket()
        self.assertEqual(get_message(sock), {'response': 200})

    def test_send_message(self):
        sock = ClientSocket()
        self.assert_(send_message(sock, {'test': 'test'}) is None)


if __name__ == '__main__':
    unittest.main()
