from socket import *
import threading

port = 2500
bufsize = 1024

#서버 소켓 생성
def echoTask(sock):
    while True:
        data = sock.recv(bufsize)
        if not data:
            break
        print('Received message: ', data.decode())
        sock.send(data)
    sock.close()

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(5)

while True:
    #클라이언트 연결 수락
    conn, (remotehost, remoteport) = sock.accept()
    print('connected by', remotehost, remoteport)

    th = threading.Thread(target=echoTask, args=(conn,))
    th.start()