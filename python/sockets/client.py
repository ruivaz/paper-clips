import socket

s = socket.socket()
host = socket.gethostname()
port = 55555

s.connect((host, port))
print s.recv(1024)
s.close
