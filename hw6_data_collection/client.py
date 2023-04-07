# Decription of client.py:
# 클라이언트는 서버 접속시 서버에 Request메시지를 보내고, 서버로부터 Success to connect를 받는다.

from socket import *
import sys

BUF_SIZE = 1024
LENGTH = 4
port = 0

while True:
    input_port = input("Choose the Device number to collect data: ")
    if input_port == '1':
        port = 8071
    elif input_port == '2':
        port = 8072
    elif input_port == 'quit':
        break
    
    
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', port))
    s.send(b'Request')
    msg = s.recv(BUF_SIZE)
    data = msg.decode()

    with open("data.txt", "a") as f:
        f.write(data+"\n")
    print("Data collection is complete")
    s.close()

