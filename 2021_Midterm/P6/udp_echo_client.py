# 손실은 클라이언트에서 서버로 보내는 경우에만 발생한다고 가정
# 서버는 40%의 확률로 응답하지 않아 손실을 발생시킴. 60%에 대해서는 ‘ack’을 전송
# 클라이언트는 서버로부터 ‘ack’을 받지 못하는 경우, 재전송 수행. 1초 간격으로 최대
# 3회 재전송 (최초 메시지 포함 최대 4번 전송)

import socket

port = 2518
BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

time = 1

while True:
    msg = input('Enter message to send : ')
    if msg =='q':
        break
    
    sock.sendto(msg.encode(),('localhost', port))
    sock.settimeout(time)
    
    try:
        data = sock.recv(BUFSIZE)
    except socket.timeout:
        time +=1
        if time >4:
            break
    else:
        data, addr = sock.recvfrom(BUFSIZE)
        print('Server says: ', data.decode())
sock.close()
    