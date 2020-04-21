# Program to transmit an HTTP Response from the Server the Browser
# HTTP Response includes : Response Header + HTML contents
# URL in the Browser : http://localhost:5000

import socket

server = socket.socket()
server.bind(('',5000))
server.listen(5)

counter = 1
while True:
    print("Waiting for client ",counter," request")
    (csoc,caddr) = x= server.accept()
    print("Request received from ",caddr)
    
    response = """HTTP/1.1 200 OK
Date: Mon, 27 Jul 2009 12:28:53 GMT
Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT
Content-Length: 71
Content-Type: text/html
Connection: Closed"""
    
    html = """
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>This is a Heading</h1>
<p>This is a paragraph.</p>
<button>OK</button>

</body>
</html>
"""
    http_resp = response+html
    http_resp = http_resp.encode()
    csoc.send(http_resp)
    print("Data sent successfully for client ",counter)
    counter = counter + 1
                    
