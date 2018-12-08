import unittest
import time
from errors import UsernameLenError, ResponseCodeError, ResponseCodeLenError, MandatoryKeyError
from client import create_presence, check_message


class TestClientCreatePresence(unittest.TestCase):

    def test_create_presence_default(self):
        self.assertEqual(create_presence(), {
        'action': 'presence',
        'time': time.time(),
        'user': {
            'account_name': 'Guest'
        }})

    def test_create_presence_with_account_name(self):
        self.assertEqual(create_presence('Test_name')['user'], {
                'account_name': 'Test_name'
            })

    def test_create_presence_with_long_account_name(self):
        with self.assertRaises(UsernameLenError):
            create_presence('123456789101112131415161718')

    def test_create_presence_with_wrong_account_name(self):
        with self.assertRaises(TypeError):
            create_presence(123)


class TestClientCheckMessage(unittest.TestCase):

    def test_check_message_not_dict_response(self):
        with self.assertRaises(TypeError):
            check_message('Test message')

    def test_check_message_not_response(self):
        with self.assertRaises(MandatoryKeyError):
            check_message({'test': 'test'})

    def test_check_message_with_wrong_len_code(self):
        with self.assertRaises(ResponseCodeLenError):
            check_message({'response': 2000})

    def test_check_message_with_wrong_code(self):
        with self.assertRaises(ResponseCodeError):
            check_message({'response': 101})

    def test_check_message_with_right_response(self):
        self.assertEqual({'response': 2000}, {'response': 2000})


if __name__ == '__main__':
    unittest.main()
