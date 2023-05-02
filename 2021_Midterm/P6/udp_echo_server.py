# 손실은 클라이언트에서 서버로 보내는 경우에만 발생한다고 가정
# 서버는 40%의 확률로 응답하지 않아 손실을 발생시킴. 60%에 대해서는 ‘ack’을 전송
# 클라이언트는 서버로부터 ‘ack’을 받지 못하는 경우, 재전송 수행. 1초 간격으로 최대
# 3회 재전송 (최초 메시지 포함 최대 4번 전송)

#udp_echo_server.py
import socket
import random

port = 7000

BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

while True:
    msg, addr = sock.recvfrom(BUFSIZE)
    print('Received : ', msg.decode())

    if random.randint(1, 10) < 4:
        print('Packet loss simulated')
        continue

    sock.sendto(msg, addr)   