
import socket
import datetime
# 포트 번호와 버퍼 사이즈를 상수로 정의
port = 2527
BUFSIZE = 1024

# 최대 재전송 횟수를 상수로 정의
MAX_RETRY = 2

# UDP 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 무한 루프
while True:
    # 메시지 입력 받기
    msg = input('Enter message to send : ')
    # 보낸 시간을 기록
    s = datetime.datetime.now()
    # 사용자가 'q'를 입력하면 루프를 빠져나옴
    if msg =='q':
        break
        
    # 메시지 전송 및 응답 대기
    retry = 0
    while retry <= MAX_RETRY:
        # 메시지 전송
        sock.sendto(msg.encode(), ('localhost', port))
        
        try:
            # 응답 대기
            sock.settimeout(1.0)
            data, addr = sock.recvfrom(BUFSIZE)
            print("Success (RTT: {})".format(datetime.datetime.now() - s))
            break
        except socket.timeout:
            # 응답이 없으면 재전송
            print('Timeout occurred, retrying...')
            retry += 1
            
    if retry > MAX_RETRY:
        # 최대 재전송 횟수를 초과하면 메시지 손실로 판단
        print('Fail')
        
# UDP 소켓 닫기
sock.close()
