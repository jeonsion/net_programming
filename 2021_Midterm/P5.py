from socket import *

port = 2500
address = ("localhost", port)
BUFSISZ = 1024

s =socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.conndect(address)

while True:
    msg = input("Enter message sned or receive: ")
    
    #msg == quit일 때 종료
    if msg == "quit":
        s.send(msg.encode())
        break
    
    