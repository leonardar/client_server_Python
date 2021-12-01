"""Unit-тесты клиента"""

import sys
import os
import unittest
from unittest.mock import patch

try:
    # python 3.4+ should use builtin unittest.mock not mock package
    from unittest.mock import patch
except ImportError:
    from mock import patch

sys.path.append(os.path.join(os.getcwd(), '../common'))
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE, DEFAULT_IP_ADDRESS, \
    DEFAULT_PORT
from client import Client, main, check_port


client = Client()

class TestClient(unittest.TestCase):

    def test_check_port_Equal(self):
        self.assertEqual(check_port(), ['127.0.0.1', 7777])

    def test_check_port_NotEqual(self):
        self.assertNotEqual(check_port(), 'В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')

    def test_check_args(self):
        server_address, server_port = check_port()
        self.assertFalse(server_port < 1024 or server_port > 65535)

    def test_parse_args(self):
        self.assertTrue(len(sys.argv) == 1 or len(sys.argv) == 3)

    def test_data_to_server(self):
        test = client.data_to_server
        test[TIME] = 1.1
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_server_responce_200(self):
        self.assertEqual(client.check_response({RESPONSE: 200}), '200 : OK')

    def test_server_response_400(self):
        self.assertEqual(client.check_response({RESPONSE: 400, ERROR: 'Bad Request'}), '400 : Bad Request')

    def test_bad_request(self):
        self.assertRaises(ValueError, client.check_response, {ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()
