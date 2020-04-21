# Server program to demonstrate how to accept connection request from Client and send the appropriate message by defining a Class

import socket, sys

class TCPServer:
	def __init__(self,portno=5000):
		self.portno = portno
		self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.sock.bind(("",self.portno))
		self.sock.listen(5)
		

	def startServer(self):
		counter = 1
		while True:
			print("\nWaiting for client "+str(counter)+" request..........")
			csock, addr = self.sock.accept()
			print("Connected to client "+str(counter))
			name = csock.recv(1024).decode('utf-8')
			msg = "Hi client "+ name + " Greeting from the Server!!"
			csock.send(msg.encode('utf-8'))
			counter += 1
			print("Connection terminated..........")

			print("\nTo accept another Client request : Enter \t  To Terminate the Server : Ctrl+C")
			try:
				user_input = input()
			except KeyboardInterrupt:
				sys.exit(0)


if __name__ == "__main__":
	server=TCPServer(6000)
	server.startServer()