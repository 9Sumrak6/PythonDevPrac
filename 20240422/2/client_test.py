import unittest
import unittest.mock as mock
import mood.client as client
from io import StringIO


class TestClientCommandParsing(unittest.TestCase):

   def test_0_move_up(self):
        with (
                mock.patch('sys.stdin', StringIO("up")),
                mock.patch('socket.socket', autospec=True) as socket_mock,
                mock.patch('mood.client.recieve', return_value=True)
             ):
            client.main()
            sendall_call = socket_mock.mock_calls[8].args[0]
            self.assertEqual(sendall_call, b'move 0 -1\n')

    def test_1_move_down(self):
        with (
                mock.patch('sys.stdin', StringIO("down")),
                mock.patch('socket.socket', autospec=True) as socket_mock,
                mock.patch('mood.client.recieve', return_value=True)
             ):
            client.main()
            sendall_call = socket_mock.mock_calls[8].args[0]
            self.assertEqual(sendall_call, b'move 0 1\n')

    def test_2_attack_tux(self):
        command = "addmon tux\nright\nleft\nattack tux"
        with (
                mock.patch('sys.stdin', StringIO(command)),
                mock.patch('socket.socket', autospec=True) as socket_mock,
                mock.patch('mood.client.recieve', return_value=True)
             ):
            client.main()
            sendall_call = socket_mock.mock_calls[8].args[0]
            self.assertEqual(sendall_call, b'addmon tux\n')
            sendall_call = socket_mock.mock_calls[9].args[0]
            self.assertEqual(sendall_call, b'move 1 0\n')
            sendall_call = socket_mock.mock_calls[10].args[0]
            self.assertEqual(sendall_call, b'move -1 0\n')
            sendall_call = socket_mock.mock_calls[11].args[0]
            self.assertEqual(sendall_call, b'attack tux\n')

    def test_3_attack_weapons(self):
        command = "attack tux with axe\nattack tux with spear\nattack tux with sword\n"
        with (
                mock.patch('sys.stdin', StringIO(command)),
                mock.patch('socket.socket', autospec=True) as socket_mock,
                mock.patch('mood.client.recieve', return_value=True)
             ):
            client.main()
            sendall_call = socket_mock.mock_calls[8].args[0]
            self.assertEqual(sendall_call, b'attack tux with axe\n')
            sendall_call = socket_mock.mock_calls[9].args[0]
            self.assertEqual(sendall_call, b'attack tux with spear\n')
            sendall_call = socket_mock.mock_calls[10].args[0]
            self.assertEqual(sendall_call, b'attack tux with sword\n')

    def test_4_attack_wrong_weapon(self):
        command = "movemonsters out\n"
        with (
                mock.patch('sys.stdin', StringIO(command)),
                mock.patch('builtins.print', autospec=True) as output_mock,
                mock.patch('socket.socket', autospec=True),
                mock.patch('mood.client.recieve', return_value=True)
             ):
            client.main()
            output_call = output_mock.mock_calls[1].args[0]
            self.assertEqual(output_call, 'Invalid command.')
