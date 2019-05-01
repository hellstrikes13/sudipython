import socket
sock = socket.socket()
host = "think-bot"
port = 12345
sock.connect((host,port))
print sock.recv(1024)
sock.close()
