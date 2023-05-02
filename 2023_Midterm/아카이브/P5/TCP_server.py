import socket
import random

BUF_SIZE = 1024
port = 8888

data = []

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', port))
sock.listen()

print("IoT 디바이스가 클라이언트의 요청을 기다립니다....")

while True:
    conn, addr = sock.accept()
    
    msg = conn.recv(BUF_SIZE)
    if not msg:
        conn.close()
        continue
    else:
        print("클라이언트로부터 메시지 {} 을(를) 입력받았습내다. :".format(msg.decode()))
    
    command = msg.decode()
    
    Temp = 0
    Humid = 0
    Lumi = 0
    #명령어에 맞게 정보를 전달한다.
    if command == "1":
        Temp = random.randint(0, 50)
    elif command == "2":
        Humid = random.randint(0, 100)
    elif command =="3" :
        Lumi = random.randint(0, 150)
    
    #4바이트 형태로 정수를 전송한다.
    # Temp = int.to_bytes(Temp, 4, byteorder='big')
    # Humid = int.to_bytes(Humid, 4, byteorder='big')
    # Lumi = int.to_bytes(Lumi, 4, byteorder='big')
    
    Temp = socket.htonl(Temp)
    Humid = socket.htonl(Humid)
    Lumi = socket.htonl(Lumi)
    
    data = "{} {} {}".format(Temp, Humid, Lumi)
    print("보내는 메시지 : ",data)
    conn.send(data.encode())

    
        