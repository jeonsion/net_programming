import socket

UDP_IP = "localhost"
UDP_PORT = 5007

# 최대 재전송 횟수를 상수로 정의
MAX_RETRY = 3

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Enter command: ")
    if message == "quit":
        break
    
    retry = 0
    while retry <=MAX_RETRY:
        sock.sendto(message.encode(), (UDP_IP, UDP_PORT))

    
        try : 
            socket.timeout(2.0) # 2초간 대기
            data, addr = sock.recvfrom(1024)
            response = data.decode()
            print(response)
            break
        except socket.timeout:
            retry+=1
    
    if retry > MAX_RETRY:
        print("Max retries exceeded, message lost")
    


sock.close()
