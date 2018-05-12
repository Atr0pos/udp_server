import socket
import threading
import json

UDP_IP = "127.0.0.1"
UDP_PORT = 5656

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(UDP_IP, UDP_PORT)

players = {}


udp_server = UdpServer(sock)
udp_server.start()

while True:
	for player in players:
		sock.sendto(data, player)
		pass
	pass	


class UdpServer(Thread):
	"""docstring for UdpServer"""
	def __init__(self, sock):

		#Start the thread as required by: 
		#https://docs.python.org/3/library/threading.html#thread-objects
		Thread.__init__(self)

		self.socket = sock
		
	def run():
		while True:
			data, addr = socket.recvfrom(1024)

			if not addr in players:
				players[addr] = {"transform" : json.dumps(data)["transform"]}
				pass
			pass