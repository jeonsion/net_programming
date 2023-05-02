from socket import *
import struct

def unpack_Udphdr(buffer):
    unpacked = struct.unpack('!HHbbbbi  ', buffer[:24])
    return unpacked




BUF_SIZE = 1024
port = 8720

while True:
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', port))
    msg = s.recv(BUF_SIZE) #    서버에 접속했을 때 Hello를 받는다.
    print(msg.decode())
    
    data = s.recv(BUF_SIZE)
    unpack_data = unpack_Udphdr(data)
    print("Sender : {}, Reciver : {}, Lumi : {}, Humi:{}, Temp : {}, Air : {}, Seq : {}".format(unpack_data[0], unpack_data[1], unpack_data[2], unpack_data[3], unpack_data[4], unpack_data[5], unpack_data[6]))
    s.close()
    
