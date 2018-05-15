import socket
import json

test3

UDP_IP = "127.0.0.1"
UDP_PORT = 5656

sock = socket.socket(	socket.AF_INET, 
						socket.SOCK_DGRAM	)

data = {"transform" : {"x" : 0, "y" : 0, "z" : 0}}
sock.sendto(json.dumps(data), (	UDP_IP, UDP_PORT	))

while True:
	data, addr = sock.recvfrom(1024)
	print data
	pass
