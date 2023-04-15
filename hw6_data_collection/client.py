# Decription of client.py:
# 클라이언트는 서버 접속시 서버에 Request메시지를 보내고, 서버로부터 Success to connect를 받는다.

from socket import *
import sys

BUF_SIZE = 1024
LENGTH = 4      #파일크기 4바이트
port = 0

while True:
    input_port = input("Choose the Device number to collect data: ")            #1번 디바이스, 2번 디바이스 중 하나를 선택
    if input_port == '1':
        port = 8071
    elif input_port == '2':
        port = 8072
    elif input_port == 'quit':
        break
    
    
    s = socket(AF_INET, SOCK_STREAM)    
    s.connect(('localhost', port))
    s.send(b'Request')      #서버에 Request메시지를 보낸다.
    msg = s.recv(BUF_SIZE)  #서버로부터 Success to connect를 받는다.
    data = msg.decode()     #받은 메시지를 디코딩한다.

    
    with open("data.txt", "a") as f:        #"a"가 의미하는 것은 append이다. 즉, 기존에 있던 내용에 덧붙여서 쓴다는 것이다.
        f.write(data+"\n")
    print("Data collection is complete")
    s.close()

