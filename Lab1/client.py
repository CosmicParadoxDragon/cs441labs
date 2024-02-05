from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a Server Socket
host = socket.gethostname()
port = 80
serverSocket.bind((host,port))
serverSocket.listen()

while True:
    # Establish the Connection
    print('Ready to serve ...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = # Fill in Start # Fill in End
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = # Fill in start # Fill in End
        # Send one HTTP header line into socket
        # Fill in Start
        # Fill in End
        # Send the Content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        

        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Fill in Start
        # Fill in End 
        # Close client socket
        # Fill in Start
        # Fill in End

serverSocket.close()
sys.exit() # Terminate the Program