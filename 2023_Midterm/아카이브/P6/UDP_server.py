

#udp_echo_server.py
import socket
import random

port = 2527

BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

while True:
    msg, addr = sock.recvfrom(BUFSIZE)
    msg = msg.decode()
    if msg == "ping":

        if random.randint(1, 10) < 4:
            print('Packet loss simulated')
            continue
        response = 'Pong'
        sock.sendto(response.encode(), addr)   