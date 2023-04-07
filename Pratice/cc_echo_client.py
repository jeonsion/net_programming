# Description: Echo client program

# Import socket module
import socket
BUFSIZE = 1024  # Buffer size

s = socket.create_connection(('localhost', 2502))   #소켓생성

while True:
    msg  = input("Message to send : ")  #키보드로부터 메시지를 입력받음
    s.send(msg.encode())                #입력받은 메시지를 서버로 전송
    data = s.recv(BUFSIZE)              #서버로부터 데이터를 받음
    if not data:
        break
    print("Received message: ", data.decode())  #받은 데이터를 출력

s.close()