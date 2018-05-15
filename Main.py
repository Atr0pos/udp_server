import socket
from threading import Thread
import copy
import json

class UdpServer(Thread):
	"""docstring for UdpServer"""
	def __init__(self, sock):

		#Start the thread as required by: 
		#https://docs.python.org/3/library/threading.html#thread-objects
		Thread.__init__(self)

		self.socket = sock
		
	def run(self):
		while True:
			data, addr = self.socket.recvfrom(1024)

			if not addr in players:
				players[addr] = {"transform" : json.loads(data)}
				pass
			pass

UDP_IP = "127.0.0.1"
UDP_PORT = 5656

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT))

players = {}


udp_server = UdpServer(sock)
udp_server.start()

while True:
	data = {}
	tempData = copy.deepcopy(players)
	for player in tempData:
		data[player[1]] = tempData[player]
		pass

	for player in tempData:
		sock.sendto(json.dumps(data), player)
		pass
	pass	


