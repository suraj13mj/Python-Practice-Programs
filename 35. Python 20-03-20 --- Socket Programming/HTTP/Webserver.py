# Program to implement a complete Webserver that accepts HTTP request and responds with an HTML page
# URL in the Browser : http://localhost:5000/docs/test.html

import socket, os

def getHttpRequest(csock):
    data = csock.recv(1024)
    data = data.decode()
    data = data.split('\n')
    data = data[0]

    data = data.split(' ')
    data = data[1]

    data = data.replace('/','\\')
    data = "f:\\httpworks" + data
    return data


def getHtmlContents(req):
    fh = open(req,"r")
    data = fh.read()
    fh.close()
    return data


def getFoundHeader(req):
    stat = os.stat(req)
    header = "HTTP/1.1 200 Ok\n"
    header = header + "Content-Type : text/html\n"
    header = header + "Content-Lenght : " + str(stat.st_size) +"\n\n"
    return header


def getNotFoundHeader():
    header = "HTTP/1.1 404 Not Found\n\n"
    return header



def sendHttpResponse(csock,req):
    data = ""
    if os.path.exists(req):
        header = getFoundHeader(req)
        html = getHtmlContents(req)
        data = header+html
        print(req," HTML file sent to the Client Browser.....")
    else:
        header = getNotFoundHeader()
        data = header    
        print(req," HTML file not found on the server.....")
    csock.send(data.encode())
    


def startServer():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('',5000))
    server.listen(5)

    print("*"*50)
    print("\nWaiting for client request...")
    csock,cadd = server.accept()
    print("Request received ...")

    httpreq = getHttpRequest(csock)
    sendHttpResponse(csock,httpreq)
    csock.close()




if __name__ == "__main__":
    startServer()
        
