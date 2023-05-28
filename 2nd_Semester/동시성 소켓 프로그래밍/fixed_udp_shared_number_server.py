from socket import *
import threading

port = 2502
bufsize = 1024

sharedData = 0

def thread_handler(data, addr):
    global sharedData
    lock.acquire()
    for _ in range(100000):
        sharedData += 1
    lock.release()
    print(sharedData)
    server_socket.sendto(str(sharedData).encode(), addr)

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', port))

lock = threading.Lock()

while True:
    data, addr = server_socket.recvfrom(bufsize)
    print('Connected by', addr)
    th = threading.Thread(target=thread_handler, args=(data, addr))
    th.start()

server_socket.close()
