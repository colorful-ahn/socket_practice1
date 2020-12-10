from socket import *
import urllib

serverIP = '127.0.0.1'
serverPort = 8080
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverIP, serverPort))
serverSocket.listen(1)
print("This server is ready to receive")

while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    print('request :', sentence.decode('utf-8'))
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence)
    connectionSocket.close()
