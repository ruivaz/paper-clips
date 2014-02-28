import socket
if __name__ == "__main__":
  PORT=5555
  RECV_BUFFER=4096
  HOST = socket.gethostname()

  s = socket.socket()
  s.connect((HOST, PORT))
  
  socket_list = [sys.stdin, s]

  while True:
    read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
    for input in read_sockets:
      if input == s:
        message = s.recv(RECV_BUFFER)
        print message
      else:
        my_message = sys.stdin.readLine()
        s.send(my_message)
