#!/bin/python

from socket import *
import threading
import random

def handle_client(connectionSocket, serverAddr):
    while True:
        nameAndnumber = connectionSocket.recv(1024).decode()
        text = ""
        numbers = ""
        digits = "0123456789"
        rn = random.randint(1,100)
        for i in nameAndnumber:
            if (i in digits):
                numbers += i
            else:
                text += i
        Sum = int(numbers) + rn
        toBeSent = text +","+ str(numbers)+","+str(rn) + "," + str(Sum) + "," + str(serverAddr[0])
        connectionSocket.send(str(toBeSent).encode())
        if not nameAndnumber:
            break
    connectionSocket.close()
    

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
serverAddr = serverSocket.getsockname()
print("The server is ready to receive. IP address:", serverAddr[0])

while True:
    connectionSocket, addr = serverSocket.accept()
    print("a new connection has been established From", addr)
    client_handler = threading.Thread(target=handle_client, args=(connectionSocket, serverAddr))
    client_handler.start()
