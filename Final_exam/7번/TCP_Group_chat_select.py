import socket, select
import time
import threading


socks = []
buffer = 1024
port = 2500

s_sock = socket.socket()
s_sock.bind(('', port))
s_sock.listen(5)

socks.append(s_sock)#소켓 리스트에 서버 소켓을 추가
print(str(port) + "에서 대기 중")


def handler(conn):
    while True:
        r_sock, w_sock, e_sock = select.select(socks, [], []) #읽기 이벤트 대기
        
        
        #채팅서버는 수신한 메시지를 발신자를 제외한 다른 클라이언트에게 전송한다.
        for s in r_sock : #수신 소켓 리스트 검사
            if s == s_sock: #새로운 클라이언트의 연결 요청 이벤트 발생
                c_sock, addr = s_sock.accept()
                print("Client ({}) connected".format(addr))  
                socks.append(c_sock) #연결된 클라이언트 소켓을 리스트에 추가

            else: #기존 클라이언트의 데이터 수신 발생
                data = s.recv(buffer)
                if not data:
                    s.close()
                    socks.remove(s)
                    continue
                print(time.asctime() + str(addr) + ": " + data.decode())
                
                for client in socks:
                    if client != s:
                        client.send(data)
            
            
while True:
    conn, addr = s_sock.accept()
    th = threading.Thread(target=handler, args=(conn,))
    th.daemon = True
    th.start()
        
    