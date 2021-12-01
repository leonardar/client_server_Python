import sys
import os
import unittest
sys.path.append(os.path.join(os.getcwd(), '../common'))
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE, RESPONDEFAULT_IP_ADDRESSSE
from server import Server, server_port, server_adress

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

server = Server()


class TestServer(unittest.TestCase):

    server_error = {
        RESPONDEFAULT_IP_ADDRESSSE: 400,
        ERROR: 'Bad Request'
    }

    server_ok_response = {RESPONSE: 200}

    def test_server_port(self):
        port_number = server_port()
        self.assertFalse(port_number < 1024 or port_number > 65535)

    def test_check_port_args(self):
        testargs = ['/Users/leonarda_rain/PycharmProjects/python_client_server/server.py', '-p']
        with patch.object(sys, 'argv', testargs):
            self.assertRaises(IndexError, server_port)

    def test_check_adress_args(self):
        testargs = ['/Users/leonarda_rain/PycharmProjects/python_client_server/server.py', '-a']
        with patch.object(sys, 'argv', testargs):
            self.assertRaises(IndexError, server_adress)

    def test_content_message(self):
        self.assertEqual(server.client_message_handler(
            {''}), self.server_error)

    def test_check_len_args(self):
        self.assertTrue(len(sys.argv) == 1 or len(sys.argv) == 5)

    def test_ok_check(self):
        self.assertEqual(server.client_message_handler(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}), self.server_ok_response)

    def test_no_action(self):
        self.assertEqual(server.client_message_handler(
            {TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}), self.server_error)

    def test_wrong_action(self):
        self.assertEqual(server.client_message_handler(
            {ACTION: 'Wrong', TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}), self.server_error)

    def test_no_time(self):
        self.assertEqual(server.client_message_handler(
            {ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}}), self.server_error)

    def test_no_user(self):
        self.assertEqual(server.client_message_handler(
            {ACTION: PRESENCE, TIME: '1.1'}), self.server_error)

    def test_unknown_user(self):
        self.assertEqual(server.client_message_handler(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest1'}}), self.server_error)


if __name__ == '__main__':
    unittest.main()
