import unittest
from server import presence_response
import time


class TestServer(unittest.TestCase):

    def test_presence_response_without_time(self):
        self.assertEqual(presence_response(
            {'action': 'presence', 'user': {'account_name': 'Guest'}}),
            {'response': 400, 'error': 'Не верный запрос!'}
        )

    def test_presence_response_with_time_wrong(self):
        self.assertEqual(presence_response(
            {
                'action': 'first',
                'time': time.time(),
            }),
            {'response': 400, 'error': 'Не верный запрос!'}
        )

    def test_presence_response_right(self):
        self.assertEqual(presence_response(
            {
                'action': 'presence',
                'time': time.time(),
                'user': {
                    'account_name': 'Guest'
                }
            }),
            {'response': 200}
        )


if __name__ == '__main__':
    unittest.main()