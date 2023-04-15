import socket

port = 2503
address = ("localhost", port)
BUFSISZ = 1024

s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

while True:
    msg = input("Enter message sned or receive: ")
    
    #msg == quit일 때 종료
    if msg == "quit":
        s.send(msg.encode())
        break
    s.send(msg.encode())
    data = s.recv(BUFSISZ)
    print("Received message: ", data.decode())
s.close()