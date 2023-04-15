from socket import *
import sys


port = 2500
BUFSIZE = 1024

if len(sys.argv) > 1:   # 명령행 인자가 있으면
    port = int(sys.argv[1])

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port ))
sock.listen()
conn, addr = sock.accept()
print("connected by ", addr)

while True:
    data = conn.recv(BUFSIZE)
    if not data:
        break
    print("Received message : ", data.decode())
    conn.send(data) #encoding해서 받아온 바이트 객체를 굳이 decdoe할 필요가 없다.
conn.close()
    