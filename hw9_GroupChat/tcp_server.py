#tcp를 이용한 단체 채팅 프로그램 서버
import socket
import time
import threading


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 2531))
s.listen()
print("Server Started")

clients = []     #클라이언트 목록

def handler(conn):
            # 새로운 클라이언트이면 목록에 추가
    if addr not in clients:
        print('new clients', addr)
        clients.append(conn)
    while True:
        data =  conn.recv(1024)
        if 'quit' in data.decode(): #quit이라는 문자열이 들어오면 해당 클라이언트를 목록에서 제거
            if addr in clients:
                clients.remove(conn)
                continue
        
        print(time.asctime() + str(addr) + ": " + data.decode())
        
        # 모든 클라이언트에게 메시지 전송
        for client in clients:
            if client != conn:
                client.send(data)
                

while True:
    conn, addr = s.accept()
    th = threading.Thread(target=handler, args=(conn,))
    th.daemon = True
    th.start()
