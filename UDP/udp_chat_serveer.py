from socket import *

port =3334
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))


while True:
    data, addr = sock.recvfrom(BUFSIZE)
    print("<-", data.decode())
    restp = input("->")
    sock.sendto(restp.encode(), addr)