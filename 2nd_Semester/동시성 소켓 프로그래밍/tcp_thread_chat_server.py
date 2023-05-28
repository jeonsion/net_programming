from socket import *
import threading


port = 3336
bufsize = 1024

#송신 스레드는 메인 스레드가 아닌 함수르 동작한다.
def sendTask(sock):
    while True:
        resp = input()
        print('->', resp)
        sock.send(resp.encode())
    
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', port))
s.listen(5)
conn, addr = s.accept()

th = threading.Thread(target=sendTask, args=(conn,))
th.start()

#수신 스레드는 메인 스레드이다.
while True:
    data = conn.recv(bufsize)
    print('<-', data.decode())