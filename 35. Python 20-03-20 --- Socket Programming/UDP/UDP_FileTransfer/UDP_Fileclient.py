import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_addr=("localhost",5000)

print("Connecting to Server....")
filename = input("Enter Filename:")

sock.sendto(filename.encode(),server_addr)
print("File request sent to Server")

file_status = "False"
file_status = sock.recvfrom(1024)

file_status = file_status[0].decode()

if file_status == "True":
    print("File exists in the server")
    ch = int(input("Do you to request the file contents: 1:Yes  2:No\n"))
    if ch == 1:
        sock.sendto(file_status.encode(),server_addr)
        print("File content request sent to Server")
        file_data = sock.recvfrom(1024)
        file_data = file_data[0].decode()
        print("File contents are:")
        print(file_data)
    elif ch == 2:
        sock.sendto("False".encode(),server_addr)
        print("Terminating the connection with the server.............")
else:
	print("File does not exist in the server !!")
	print("Terminating the connection with the server..............")
    



