import socket

host = 'localhost'
port = 80

# 외부 서버와 통신할 소켓
external_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 외부 서버와 통신할 소켓
external_socket.bind((host, port))

external_socket.listen()

print("외부 서버는 릴레이 서버를 기다리고 있습니다.")

while True:
    relay_conn, relay_addr = external_socket.accept()
    print("외부 서버와 릴레이 서버가 연결되었습니다.")

    # 릴레이 서버로부터 HTTP 요청을 받아서 다시 릴레이 서버에
