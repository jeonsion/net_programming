#공유 자원을 사용하는 프로그램 (서버)
# 클라이언트 접속 시, 별도 스레드를 생성하여 처리함
# 클라이언트가 접속할 때마다 공유 자원을 100000번 증가시킴

from socket import *
import threading

port = 2501
bufsize = 1024

sharedData = 0

def thread_handler(sock):
    global sharedData
    lock.acquire()
    for _ in range(100000):
        sharedData +=1
    lock.release()
    print(sharedData)
    sock.send(str(sharedData).encode())
    sock.close()

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', port))
s.listen(5)

lock = threading.Lock()

while True:
    client, addr = s.accept()
    print('Connected by', addr)
    th = threading.Thread(target=thread_handler, args=(client,))
    th.start()
    
s.close()