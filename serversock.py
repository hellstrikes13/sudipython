import socket
sock = socket.socket()
host = socket.gethostname()
port = 12345
sock.bind((host,port))
sock.listen(10)
while True:
 c,addr = sock.accept()
 print 'got connection from : ',addr
 c.send("thanks for conneting me \n\t.....I m the server....")
 c.close()

