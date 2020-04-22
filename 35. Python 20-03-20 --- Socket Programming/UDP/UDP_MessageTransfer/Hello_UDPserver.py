# Server program to demonstrate how to accept connection request from Client and send the appropriate message using UDP protocol

import socket, threading

class UDPserver(threading.Thread):
    def __init__(self,portno = 5000):
        super().__init__()
        self.portno = portno
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.sock.bind(('',self.portno))
        self.start()

    def run(self):
        counter = 1
        while True:
            print("\nWaiting  for client "+str(counter)+" request.....")
            recvdata = self.sock.recvfrom(1024)
            print("Request received from ",recvdata[1])

            msg = recvdata[0].decode()
            client_addr = recvdata[1]

            print("Client message: "+msg)

            msg = "Hello to client "+str(counter)
            msg = msg.encode()

            self.sock.sendto(msg,client_addr)
            print("Message sent to client "+str(counter))
            counter += 1



if __name__ == "__main__":
    server = UDPserver()
