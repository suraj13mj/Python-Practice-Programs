# Client program to demonstrate how to send connection request to Server

import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("localhost",5000))
print("Connection request to Server..........")

data = sock.recv(1024)
sdata = data.decode('utf-8')
print("Message from Server:"+sdata)

print("Connection closed..........")