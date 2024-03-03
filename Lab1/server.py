from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)
MAX_CONNECTIONS = 4
# Prepare a Server Socket
host = "127.0.0.1"
port = 80
serverSocket.bind((host,port))
serverSocket.listen(MAX_CONNECTIONS)


while True:
    # Establish the Connection
    print('Ready to serve ...')
    
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024) # Fill in Start # Fill in End
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.readlines()# Fill in start # Fill in End
        # Send one HTTP header line into socket
        # Fill in Start
        connectionSocket.sendall("HTTP/1.1 200 OK\r\nContent-type: text/html\r\nSet-Cookie: ServerName=lab1server\r\n\r\n".encode())
        # Fill in End
        # Send the Content of the requested file to the client
        print (outputdata)
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Fill in Start
        connectionSocket.sendall(b"HTTP/1.1 404 NOT FOUND\r\n")
        # Fill in End 
        # Close client socket
        # Fill in Start
        connectionSocket.close()
        # Fill in End

serverSocket.close()
sys.exit() # Terminate the Program
