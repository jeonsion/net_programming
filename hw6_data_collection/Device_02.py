#Device_01 Decription:
#클라이언트와 서버가 연결될시 서버는 Hello를 입력받고, 클라이언트에게 Success to connect를 보낸다.

from socket import *
import os
import datetime
import random

#시간을 형식에 맞게 출력하기 위한 코드 -----------------------
now = datetime.datetime.now()
formatted_time = now.strftime("%a %b %d %H:%M:%S %Y")
#____________________________________________________


BUF_SIZE = 1024
LENGHT = 4  #파일크기 4바이트
data = []
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('localhost', 8072))  #Device_02의 포트번호는 8072
sock.listen()
print("IoT Device 02 is running...")

while True:
    conn, addr = sock.accept()
    
    msg = conn.recv(BUF_SIZE)
    if not msg:
        conn.close()
        continue
    else:
        print('Accept the client\'s request : ', msg.decode()) # Hello
    command = msg.decode()
    
    if command == 'Request':
        temp = random.randint(40, 140)
        humid = random.randint(2000, 6000)
        illuminance = random.randint(1000, 4000)
        data = "{}: Device2: Heartbeat: {}, Steps: {}, Cal: {}".format(formatted_time,temp, humid, illuminance)
        conn.send(data.encode())
        print("Send the data to the client")
    elif command == 'quit':
        print("Exit the client")
    conn.close()    
    