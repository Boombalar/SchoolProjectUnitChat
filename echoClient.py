import socket

HOST = 'localhost'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
while True:
    inputString = raw_input("echo> ")
    if (inputString == "quit" or inputString == "exit"):
        break
    s.sendall(inputString)
    data = s.recv(1024)
    print('Received', repr(data))
s.close()

