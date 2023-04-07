#Device_01 Decription:
#클라이언트와 서버가 연결될시 서버는 Hello를 입력받고, 클라이언트에게 Success to connect를 보낸다.

from socket import *
import os
import datetime
import random

now = datetime.datetime.now()
formatted_time = now.strftime("%a %b %d %H:%M:%S %Y")


BUF_SIZE = 1024
LENGHT = 4
data = []
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('localhost', 8071))
sock.listen()
print("IoT Device 01 is running...")

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
        temp = random.randint(0, 40)
        humid = random.randint(0, 100)
        illuminance = random.randint(70, 150)
        data = "{}: Device1: Temp: {}, Humid: {}, Illuminance: {}".format(formatted_time,temp, humid, illuminance)
        conn.send(data.encode())
        print("Send the data to the client")
    elif command == 'quit':
        print("Exit the client")
    conn.close()