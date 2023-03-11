import socket

# this will accept the connections
s = socket.socket()
print("socket created")

s.bind(("localhost", 9999))
s.listen(3)
print("listening to connections")

while True:
    clientSocket, address = s.accept()
    name = clientSocket.recv(1024).decode()
    print("connected with ", address, name)
    clientSocket.send(bytes("Welcome to socket",'utf-8'))
    clientSocket.close()



