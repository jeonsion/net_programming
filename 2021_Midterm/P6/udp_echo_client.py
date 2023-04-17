# 손실은 클라이언트에서 서버로 보내는 경우에만 발생한다고 가정
# 서버는 40%의 확률로 응답하지 않아 손실을 발생시킴. 60%에 대해서는 ‘ack’을 전송
# 클라이언트는 서버로부터 ‘ack’을 받지 못하는 경우, 재전송 수행. 1초 간격으로 최대
# 3회 재전송 (최초 메시지 포함 최대 4번 전송)
import socket

# 포트 번호와 버퍼 사이즈를 상수로 정의
port = 2527
BUFSIZE = 1024

# 최대 재전송 횟수를 상수로 정의
MAX_RETRY = 3

# UDP 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 무한 루프
while True:
    # 메시지 입력 받기
    msg = input('Enter message to send : ')
    
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
            
            # 서버로부터 응답이 왔으면 응답 내용 출력
            print('Server says: ', data.decode())
            break
        except socket.timeout:
            # 응답이 없으면 재전송
            print('Timeout occurred, retrying...')
            retry += 1
            
    if retry > MAX_RETRY:
        # 최대 재전송 횟수를 초과하면 메시지 손실로 판단
        print('Max retries exceeded, message lost')
        
# UDP 소켓 닫기
sock.close()
