from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(2)
input_string = []
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept ()
    sentence = connectionSocket.recv(1024).decode ()
    #capitalizedSentence = sentence.upper()
    input_string.append(sentence)
    #connectionSocket.send(capitalizedSentence.encode()),
    #connectionSocket.close()
    if len(input_string) == 2:
        connectionSocket.send(input_string[0].encode())
        connectionSocket.close()