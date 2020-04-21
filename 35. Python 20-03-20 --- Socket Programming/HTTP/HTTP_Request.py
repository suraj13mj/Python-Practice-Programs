#Program to display the HTTP Request Header in the console transmitted by the Browser to the Server
#URL in the Browser : http://localhost:5000

import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('',5000))
sock.listen(5)

counter = 1

while True:
    print("Waiting for client "+str(counter)+" request.......")
    csock,cadd = sock.accept()
    print("Request received from client IP : "+str(cadd))

    st = ""
    print("Request is .............................................")
    while True:
        data = csock.recv(1024)
        sdata = data.decode()
        print(sdata)
        break
    print("Request end.............................................")

    csock.close()
    print("Client "+str(counter)+" connection closed")
    

    counter = counter + 1
                        
    
