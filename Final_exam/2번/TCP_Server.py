import socket, select

socks = []
buffer = 1024
port = 7777

s_sock = socket.socket()
s_sock.bind(('', port))
s_sock.listen(5)

socks.append(s_sock)#소켓 리스트에 서버 소켓을 추가
print(str(port) + "에서 대기 중")

while True:
    r_sock, w_sock, e_sock = select.select(socks, [], []) #읽기 이벤트 대기
    
    for s in r_sock : #수신 소켓 리스트 검사
        if s == s_sock: #새로운 클라이언트의 연결 요청 이벤트 발생
            c_sock, addr = s_sock.accept()
            socks.append(c_sock) #연결된 클라이언트 소켓을 리스트에 추가
            print("Client ({}) connected".format(addr))
        else:
            data = s.recv(buffer)
            if not data:             
                s.close()
                socks.remove(s) #연결 종료된 클라이언트 소켓을 리스트에서 제거
                continue
            #서버로부터 1 25가 들어오면 split을 통해 1과 25로 나누어진다. 그리고 딕셔너리 형태로 저장한다.
            else:
                data = data.decode().split()
                #딕셔너리 형태로 저장
                if data[0] == '1':
                    #딕셔너리 형태로 저장
                    
                
            print("Received data : " + data.decode())
            s.send(data)
            