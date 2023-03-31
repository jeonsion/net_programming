import socket

HOST = 'localhost'  # 서버 IP 주소 또는 도메인
PORT = 8888         # 서버 포트 번호

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        user_input = input("계산할 수식을 입력하세요(q: 종료): ")
        if user_input == "q":
            break

        s.sendall(user_input.encode())
        result = s.recv(1024).decode()

        print(f"결과: {result}")
