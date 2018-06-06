import select
import socket
from threading import Thread, Lock
import copy
import json

class UdpSender(Thread):
	"""docstring for UdpServer"""
	def __init__(self, sock, lock):

		#Start the thread as required by: 
		#https://docs.python.org/3/library/threading.html#thread-objects
		Thread.__init__(self)

		self.socket = sock
		self.messageQueue = {}
		
	def run(self):
		potential_readers = [self.socket]
		potential_writers = []

		while True:
			lock.acquire()

			for addr in players:
				
				self.socket.sendto(players[addr], addr)
				pass
				
			lock.release()	

class TcpServer(Thread):
	def __init__(self, TCP_PORT, TCP_IP, sock, lock):
		#Start the thread as required by: 
		#https://docs.python.org/3/library/threading.html#thread-objects
		Thread.__init__(self)

		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.bind((TCP_IP, TCP_PORT))
		self.socket.setblocking(0)
		self.socket.settimeout(5)
		pass

	def run(self):
		self.socket.listen(10)

		while True:
			conn, addr = sock.accept()

			print "New TCP connection from ", addr

			data = conn.recv(1024)
			if data == "login":
				
			pass
		pass

class UdpServer(Thread):
	"""docstring for UdpServer"""
	def __init__(self, sock, lock):

		#Start the thread as required by: 
		#https://docs.python.org/3/library/threading.html#thread-objects
		Thread.__init__(self)

		self.socket = sock
		self.messageQueue = {}
		
	def run(self):
		potential_readers = [self.socket]
		potential_writers = []

		while True:
			data, addr = self.socket.recvfrom(1024)
			if addr not in players:
				lock.acquire()
				players[addr] = data

				lock.release()
			self.socket.sendto(data, addr)
			
UDP_IP = "127.0.0.1"
UDP_PORT = 5656

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.setblocking(0)
sock.bind((UDP_IP, UDP_PORT))

players = {}

lock = Lock()

udp_server = UdpServer(sock, lock)
udp_sender = UdpSender(sock, lock)
udp_server.start()
# udp_sender.start()

print 'Server ready....'

# while True:
# 	data = {}
# 	tempData = copy.deepcopy(players)
# 	for player in tempData:
# 		data[player[1]] = tempData[player]
# 		pass

# 	for player in tempData:
# 		sock.sendto(json.dumps(data), player)
# 		pass
# 	pass	


