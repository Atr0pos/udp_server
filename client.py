import socket
import json
from datetime import datetime


UDP_IP = "127.0.0.1"
UDP_PORT = 5656

sock = socket.socket(	socket.AF_INET, 
						socket.SOCK_DGRAM	)

data = "ping"


while True:
	time 		= datetime.now()
	sock.sendto(data, (	UDP_IP, UDP_PORT	))
	data, addr = sock.recvfrom(1024)
	presentTime = datetime.now()
	print (presentTime - time).total_seconds() * 1000.0
	pass
