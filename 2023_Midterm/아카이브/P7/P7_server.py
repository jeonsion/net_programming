from socket import *
import random
import struct

Buf_SIZE = 1024
port = 8720

data = []

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('localhost', port))
sock.listen()

while True:
    conn, addr = sock.accept()
    conn.send(b"Hello") #    클라이언트가 접속하면 Hello를 보낸다.
    
    sender = random.randint(1,50000)
    receiver = random.randint(1,50000)
    Lumi = random.randint(1,100)
    Humi = random.randint(1,100)
    Temp = random.randint(1,100)
    Air = random.randint(1,100)
    seq = random.randint(1,100000)
    
    packed = b''
    packed += struct.pack('!HH', sender, receiver)
    packed += struct.pack('!bbbb', Lumi, Humi, Temp, Air)
    packed += struct.pack('!i', seq)
    
    conn.send(packed)
    conn.close()