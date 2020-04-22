# Server program to demonstrate how to perform file transfer from Server using TCP protocol
# Server code

import socket, sys

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('',5000))
sock.listen(5)

counter = 1

while True:
    print("Waiting for client "+str(counter)+" request..........")
    csock,cadd = sock.accept()
    print("Request received from client IP : "+str(cadd))

    fh = open('datafile.txt','r')

    for line in fh:
        bdata = line.encode('utf-8')
        csock.send(bdata)

    print("File upoaded successfully to client "+str(counter))
    csock.close()
    print("Client "+str(counter)+" connection closed")
    counter = counter + 1
    print("\nTo accept another Client request : Enter \t  To Terminate the Server : Ctrl+C")

    try:
        user_input=input()
    except KeyboardInterrupt:
        sys.exit(0)
                        
    

                        
    
