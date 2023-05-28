from socket import *

port = 2501
bufsize = 1024

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', port))

print(int(s.recv(bufsize).decode()))

s.close()