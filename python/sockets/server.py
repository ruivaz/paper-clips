import socket, select

def broadcast(sock, message):
  for socket_local in CONNECTION_LIST:
    if socket_local!=s and socket_local!=sock:
      try:
        socket_local.send(message)
      except:
	socket.close()
	CONNECTION_LIST.remove(socket)


if __name__ == "__main__": 
  PORT=5555
  RECV_BUFFER=4096
  HOST = socket.gethostname()

  CONNECTION_LIST = []

  s = socket.socket()
  CONNECTION_LIST.append(s)

  s.bind((HOST, PORT))
  s.listen(15)
  print 'Chat Server Started on ' + str(PORT)


  while True:
    read_sockets, write_sockets, error_socket = select.select(CONNECTION_LIST, [], [])
    for socket in read_sockets:
      #New Connection from Client
      if socket not in CONNECTION_LIST:
        c, addr = s.accept()
        CONNECTION_LIST.append(c)
        print 'New User: ', addr
      else:
        try:
	  message = socket.recv(RECV_BUFFER)
          if message:
            broadcast(socket, message)
        except: 
            broadcast(socket, "Client (%s, %s) is offline" % addr)
            print 'Client (%s, %s) is offline' % addr
            socket.close()
            CONNECTION_LIST.remove(socket) 
            continue
            
        
  server_socket.close()     
