#!/bin/python3

from socket import *
serverName = '192.168.43.197'
serverPort = 12003
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
while True:
  cliInput = input('Input your name and a random number between 1 to 100:')
  clientSocket.send(cliInput.encode())
  from_server= clientSocket.recv(1024)
  result = from_server.decode()
  result_arr = result.split(',')
  for i in range(0,len(result_arr)):
            print (result_arr[i])
clientSocket.close()
