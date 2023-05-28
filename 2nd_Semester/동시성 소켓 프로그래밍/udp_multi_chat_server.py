#UDP를 이용한 단체 채팅 프로그램 만들기 서버
#채팅 서버는 수신한 메시지를 발신자를 제외한 다른 클라이언트에게 전송
#새로운 클라이언트가 들어오면 클라이언트 목록에 저장
#채팅 클라이언트가 'quit'를 전송하면 해당 클라이언트를 목록에서 삭제

import socket
import time

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 2500))

print('Server started')

while True:
    data, addr = s.recvfrom(1024)
    #quit를 수신하면 해당 클라이언트를 목록에서 삭제
    
    if 'quit' in data.decode():
        if addr in clients:
            print(addr, 'exited')
            clients.remove(addr)
            continue
    
    #새로운 클라이언트면 목록에 추가
    if addr not in clients:
        print('new client', addr)
        clients.append(addr)
        
    print(time.asctime() + str(addr) + ':' + data.decode())
    
    #수신한 메시지를 다른 클라이언트에게 전송 (자기를 제외하고)
    for client in clients:
        if client != addr:
            s.sendto(data,client)