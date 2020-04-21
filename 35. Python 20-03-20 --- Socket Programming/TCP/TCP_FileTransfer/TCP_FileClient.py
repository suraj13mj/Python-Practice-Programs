# Client program to demonstrate how to request for a file from the Server
# Client code

import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print("Connecting to the server.....")
sock.connect(('localhost',5000))
print("Connected successfully")

fh = open('f:\\httpworks\\docs\\datafile.txt','w')

while True:
    line = sock.recv(1024)
    sdata = line.decode('utf-8')
    if not sdata:
        break
    fh.write(sdata)
    

print("File downloaded successfully")
sock.close()
print("Connection closed")


