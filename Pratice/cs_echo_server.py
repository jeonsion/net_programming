#필요한 라이브러리 import
from socket import *

port = 2502  #포트번호
BUFSIZE = 1024 #버퍼사이즈

sock = create_server(('localhost', port), family=AF_INET, backlog=1)    #소켓생성
conn, (remotehost, remoteport) = sock.accept() #클라이언트의 접속을 기다림
print('connected by ', remotehost, remoteport) #클라이언트의 접속정보 출력

while True :    
    data = conn.recv(BUFSIZE)                        #클라이언트로부터 데이터를 받음
    if not data :                                    #데이터가 없으면 반복문을 빠져나감
        break
    print("received message: ", data.decode())       #받은 데이터를 출력
    conn.send(data)                                  #클라이언트로 데이터를 보냄 
conn.close()                                         #소켓을 닫음


