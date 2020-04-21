# Client program to demonstrate how to send connection request to Server and message (name) to the Server

import socket

sock=socket.socket()
sock.connect(("localhost",6000))
print("Connected Successfully to the Server")

name = input("Enter your Name:")
sock.send(name.encode())
print(sock.recv(1024).decode())
sock.close