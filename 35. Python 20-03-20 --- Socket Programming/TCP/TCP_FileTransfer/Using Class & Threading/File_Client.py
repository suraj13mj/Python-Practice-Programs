# Client program to demonstrate how to request for a file from the Server using Classes and Multithreading
# Client code

import socket, threading

class FTPClient(threading.Thread):
	def __init__(self,serverip,portno,filename):
		super().__init__()
		self.serverip = serverip
		self.portno = portno
		self.filename = filename
		self.sock = socket.socket()
		self.start()

	def run(self):
		self.sock.connect((self.serverip,self.portno))
		self.sock.send(self.filename.encode('utf-8'))
		print("Connected to Server.....")
		fh=open("f:\\httpworks\\"+self.filename,"w")

		while True:
			bline = self.sock.recv(1024)
			line = bline.decode()
			if not line:
				break
			fh.write(line)
		fh.close()

		self.sock.close()
		print("File downloaded.....")


if __name__ == "__main__":
	serverip = input("Enter Server IP:")
	portno = int(input("Enter Portno:"))
	filename = input("Enter filename to download:")

	download = FTPClient(serverip,portno,filename)