import socket 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9003)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())
SendMsg = "sionJeon"
sock.send(SendMsg.encode())


#int.from_bytes()는 4바이트를 받아야함
msg = int.from_bytes(sock.recv(1024), 'big')
print(msg)

sock.close()

