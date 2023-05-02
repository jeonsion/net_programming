
import socket
import sys

BUF_SIZE = 1024
port = 8888

while True:

    input_num = input("숫자를 입려하세요 : ")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', port))
    
    #서버에 숫자를 전송한다.
    s.send(input_num.encode())
    
    #서버로부터 메시지를 받는다.
    msg =s.recv(BUF_SIZE).decode()
    Temp, Humid, Lumi = map(int, msg.split())
    m_Temp = socket.ntohl(Temp)
    m_Humid = socket.ntohl(Humid)
    m_Lumi = socket.ntohl(Lumi)
    print("Temp : {}, Humid : {}, Lumi : {}".format(m_Temp, m_Humid, m_Lumi))
    