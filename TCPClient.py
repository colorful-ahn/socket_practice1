from socket import *

serverIP = '127.0.0.1'

serverPort = 8080



while 1:

	clientSocket = socket(AF_INET, SOCK_STREAM)

	clientSocket.connect((serverIP,serverPort))

	sentence = input('Input lowercase sentence:')

	clientSocket.send(sentence.encode())

	modifiedSentence = clientSocket.recv(1024)

	print('From Server:', modifiedSentence.decode())

	clientSocket.close()

