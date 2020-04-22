# Server program to demonstrate how to perform file transfer from Server to Client using UDP protocol
# Server code

import socket,os

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(("",5000))

counter=1

while True:
    print("\nWaiting for Client "+str(counter)+" request........................")
    recv_req = sock.recvfrom(1024)
    client_addr = recv_req[1]
    print("Request received from ",client_addr)

    recv_req_file = "F:\\httpworks\\docs\\"
    recv_req_file += recv_req[0].decode('utf-8')


    if os.path.exists(recv_req_file):
        file_status = "True"
    else:
        file_status= "False"
        print("File does not exist !!")

    sock.sendto(file_status.encode(),client_addr)
    print("File status sent to the client")

    if file_status == "True":
        recv_ack = sock.recvfrom(1024)
        recv_ack = recv_ack[0].decode()
        if recv_ack == "True":
            fh=open(recv_req_file,"r")
            data=fh.read()
            fh.close()
            print(data)
            sock.sendto(data.encode(),client_addr)
            print("File contents sent to the Client"+str(counter))
            print("Connection Terminated...............................")
        elif recv_ack == "False":
            print("Connection Terminated...............................")

    counter+=1

    




    




    