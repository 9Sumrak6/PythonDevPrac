#!/usr/bin/env python3
'''
'''

import unittest
import multiprocessing
import socket
import cowsay
import time

import start_server

def send_cmd(cmd, sock):
	sock.sendall((cmd + "\n").encode())
	# print(cmd)
	ans = sock.recv(1024).decode()
	# print(ans)
	# print("Moved to (1, 0)\n" + cowsay.cowsay("it is me, hi", cow='tux'))
	return ans

class TestServer(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.proc = multiprocessing.Process(target=start_server.serve)
		cls.proc.start()
		time.sleep(1)

	@classmethod
	def tearDownClass(cls):
		cls.proc.terminate()
		cls.proc.join()

	def setUp(self):
		host = "localhost"
		port = 1337

		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect((host, port))

		self.socket.sendall("me\n".encode())
		self.socket.recv(1024).decode()

	def tearDown(self):
		self.socket.close()

	def test_0_test_server(self):
		self.assertEqual(send_cmd("movemonsters off", self.socket), 'Moving monsters: off\n')

	def test_1_test_server(self):
		self.assertEqual(send_cmd("addmon tux coords 1 0 hello it is me, hi hp 100", self.socket), '"me" added tux to (1, 0) saying it is me, hi with hp = 100\n')

	def test_2_test_server(self):
		self.assertEqual(send_cmd("addmon tux", self.socket), '"me" added tux to (0, 0) saying Hello with hp = 100\n')

	def test_3_test_server(self):
		self.assertEqual(send_cmd("move 1 0", self.socket), "Moved to (1, 0)\n" + cowsay.cowsay("it is me, hi", cow='tux'))

	def test_4_test_server(self):
		self.assertEqual(send_cmd("attack tux", self.socket), '"me" attacked tux,  damage 10 hp\ntux now has 90 hp.\n')

	def test_5_test_server(self):
		self.assertEqual(send_cmd("attack tux with axe", self.socket), '"me" attacked tux,  damage 20 hp\ntux now has 70 hp.\n')
