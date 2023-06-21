#TCP를 이용한 단체 채팅 프로그램 만들기 (클라이언트)
import socket
import threading

def handler(sock):
    while True:
        msg = sock.recv(1024)
        print(msg.decode())
        
svr_addr = ('localhost', 2500)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(svr_addr)

my_id = input('ID를 입력하세요: ')
sock.send(('[' + my_id + ']').encode())



while True:
    th  = threading.Thread(target=handler, args=(sock,))
    th.daemon = True
    th.start()
    msg = '[' + my_id + '] ' + input()
    sock.send(msg.encode())
