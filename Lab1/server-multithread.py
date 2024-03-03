from socket import *
import sys
import threading

MAX_CONNECTIONS = 4
host = "127.0.0.1"
port = 80
HTML_Header = "HTTP/1.1 200 OK\r\nContent-type: text/html\r\nSet-Cookie: ServerName=lab1server\r\n\r\n"

def main():

    try:
        # Prepare a Server Socket
        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.bind((host,port))
        serverSocket.listen()
        print(f'Ready to serve on {host}:{port}...')
        while True:

            connectionSocket, addr = serverSocket.accept()
            print(f"Connection on {addr[0]}:{addr[1]}")
            thread = threading.Thread(target=handle_connection, args=(connectionSocket, addr))
            thread.start()
    
    except Exception as e:
        print(e)
        
    sys.exit() # Terminate the Program

def handle_connection(connectionSocket, addr):
    try:
        message = connectionSocket.recv(1024) # Fill in Start # Fill in End
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.readlines()# Fill in start # Fill in End
        # Send one HTTP header line into socket
        # Fill in Start
        connectionSocket.sendall(HTML_Header.encode())
        # Fill in End
        # Send the Content of the requested file to the client
        print (outputdata)
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
    except IOError:
        # Send response message for file not found
        # Fill in Start
        connectionSocket.sendall(b"HTTP/1.1 404 NOT FOUND\r\n")
        # Fill in End 
    connectionSocket.close()


if __name__ == "__main__":
    main()