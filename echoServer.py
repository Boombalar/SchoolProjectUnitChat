import socket

HOST = ''
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn, addr = s.accept()
print('Connected by' + addr[0])
while True:
    data = conn.recv(1024)
    if data:
        print("Recieved " + data)
        if data == "STOP":
            conn.close()
            break
    conn.sendall(data)
