from socket import *
import random
port = 7000
BUFSIZE = 1024


sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))
dict = {}
while True:
    #클라이언트로부터 데이터를 받는다.
    data, addr = sock.recvfrom(BUFSIZE)
    
    #클라이언트로부터 받은 데이터를 저장한다.
    data = data.decode()
    if data == "quit":
        break
    
    split_data = data.split()
    Type = split_data[0]    #type 추출
    mboxId = split_data[1]  #mboxid 추출
    message = " ".join(split_data[2:])  #message 추출

    #클라이언트로부터 받은 데이터가 send이면
    if Type == "send":
        if mboxId in dict:          #딕셔너리에 mboxId가 있으면
            dict[mboxId].append(message)   #딕셔너리에 mboxId의 message를 추가한다.
        else:
            dict[mboxId] = [message]    #딕셔너리에 mboxId가 없으면 mboxId와 message를 추가한다.
        sock.sendto("OK".encode(), addr)    #클라이언트에게 OK를 보낸다.
    elif Type == "receive":
        if mboxId in dict:
            if len(dict[mboxId]) > 0 :
                send_message = dict[mboxId][0]
                del dict[mboxId][0]
                sock.sendto(send_message.encode(), addr)
            else:
                sock.sendto("No message".encode(), addr)
        else:
            sock.sendto("No message".encode(), addr)
sock.close()
