import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost',  9100)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())
#이름 문자열 전송
sock.send(b"Sion Jeon")
#학번 수신 후 출력
msg = int.from_bytes(sock.recv(1024), 'big')
print(msg)
sock.close()