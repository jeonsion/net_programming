from socket import *

port = 2502
bufsize = 1024

client_socket = socket(AF_INET, SOCK_DGRAM)

client_socket.sendto(''.encode(), ('localhost', port))

data, server_addr = client_socket.recvfrom(bufsize)
print(int(data.decode()))

client_socket.close()
