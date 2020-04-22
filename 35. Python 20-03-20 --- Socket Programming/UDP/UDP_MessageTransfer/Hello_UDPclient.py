# Client program to demonstrate how to send connection request to Server using UDP protocol

import socket, threading

class UDPclient(threading.Thread):
	def __init__(self,server_ip="localhost",server_port=5000):
		super().__init__()
		self.server_addr = (server_ip,server_port)
		self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		self.start()

	def run(self):
		d_msg = " ".encode()
		self.sock.sendto(d_msg,self.server_addr)
		print("Connecting to Server.....")
		recvdata = self.sock.recvfrom(1024)
		msg = recvdata[0].decode()
		print("Server Message: "+msg)
		print("Connection closed.....")

if __name__ == "__main__":
	client = UDPclient("127.0.0.1",5000)