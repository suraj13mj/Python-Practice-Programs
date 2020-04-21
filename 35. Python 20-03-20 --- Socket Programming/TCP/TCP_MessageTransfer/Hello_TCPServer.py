# Server program to demonstrate how to accept connection request from Client and send the appropriate message 

import socket, sys

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("",5000))
sock.listen(5)

counter=1

while True:
	print("\nWaiting for client "+str(counter)+" request..........")
	csock,caddr = sock.accept()

	data = "Hello World from Server to Client "+str(counter)

	bdata = data.encode('utf-8')
	csock.send(bdata)
	csock.close()

	print("Data transmitted to client "+str(counter))
	print("Client "+str(counter)+" connection closed..........")

	counter += 1

	print("\nTo accept another Client request : Enter \t  To Terminate the Server : Ctrl+C")
	try:
		user_input = input()
	except KeyboardInterrupt:
		sys.exit(0)

