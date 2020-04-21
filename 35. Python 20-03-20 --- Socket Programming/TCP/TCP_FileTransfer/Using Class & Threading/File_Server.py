# Server program to demonstrate how to perform file transfer from Server using Classes and Multithreading
# Server code

import socket, threading, sys
lck=threading.Lock()

class FTPServer(threading.Thread):
	def __init__(self,portno = 5000):
		super().__init__()
		self.portno = portno
		self.sock = socket.socket()
		self.sock.bind(('',self.portno))
		self.sock.listen(5)
		self.start()

	def run(self):
		while True:
			print("\nWaiting for client request.....")
			csoc, addr = self.sock.accept()
			print("Connected to client :",addr)
			
			upload = UploadServerThread(csoc)
			upload.start()
			upload.join()



class UploadServerThread(threading.Thread):
	def __init__(self,csoc):
		super().__init__()
		self.csoc = csoc


	def run(self):
		filename = self.csoc.recv(1024).decode('utf-8')
		print("Requested file:",filename)
		fh=open(filename,"r")

		while True:
			line = fh.readline()
			if not line:
				break
			self.csoc.send(line.encode())
		fh.close()
		self.csoc.close()
		print("File Uploaded successfully.....")
		



if __name__ == "__main__":
	ftpserver = FTPServer()