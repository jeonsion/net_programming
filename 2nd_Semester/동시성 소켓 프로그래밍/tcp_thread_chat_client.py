from socket import *
import threading

port = 3336
bufsize = 1024

#수신 스레드는 함수로 구현한다.
def recvTask(sock):
    while True:
        data = sock.recv(bufsize)
        print('<-', data.decode())

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', port))

th = threading.Thread(target=recvTask, args=(sock,))
th.start()

while True:
    msg = input()
    print('->', msg)
    sock.send(msg.encode())