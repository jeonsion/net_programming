import socket

def calculate(data):
    try:
        # 공백을 기준으로 피연산자와 연산자 분리
        operand1, operator, operand2 = data.split()
        # 피연산자를 정수형으로 변환
        operand1 = int(operand1)
        operand2 = int(operand2)
        # 연산자에 따라 계산
        if operator == "+":
            result = operand1 + operand2
        elif operator == "-":
            result = operand1 - operand2
        elif operator == "*":
            result = operand1 * operand2
        elif operator == "/":
            result = round(operand1 / operand2, 1)
        else:
            result = "지원하지 않는 연산자입니다."

        return result

    except ValueError:
        return "잘못된 입력입니다."

HOST = ''    # 모든 인터페이스에서 연결 요청 수신
PORT = 8888  # 사용할 포트

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    print(f"서버가 {PORT}번 포트에서 시작되었습니다.")

    while True:
        conn, addr = s.accept()
        with conn:
            print(f"{addr}에서 연결이 수락되었습니다.")

            while True:
                data = conn.recv(1024).decode()

                if not data:
                    break

                result = calculate(data)

                conn.sendall(str(result).encode())

                print(f"{addr}: {data} = {result}")

                if data.strip() == "q":
                    break
