import socket
import os


# 웹 서버 호스트와 포트번호 설정
HOST = ''
PORT = 80

# HTTP 응답 헤더 및 바디
HTTP_RESPONSE_200_OK = "HTTP/1.1 200 OK\r\nContent-Type: {}\r\n\r\n"
HTTP_RESPONSE_404_NOT_FOUND_HEAD = "HTTP/1.1 404 Not Found\r\n\r\n"
HTTP_RESPONSE_404_NOT_FOUND_BODY = "<HTML><HEAD>\n<TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>"

# 서버 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

while True:
    # 클라이언트 연결 대기
    conn, addr = server_socket.accept()
    print('Connected by', addr)

    # 클라이언트 요청 수신
    request_data = conn.recv(1024).decode()
    
    # 요청 데이터 파싱 request_lines는 GET /index.html HTTP/1.1의 형식을 가진다.
    request_lines = request_data.split('\r\n')
    method, filename, protocol = request_lines[0].split(' ')
    
    #method, filename, protocol 중에서 filename만 추출
    filename = filename[1:]

    
    #ico는 Not Found에도 불구하고 띄워줘야 하므로 따로 빼준다.
    if filename.endswith('.ico'):
            f=open(filename, 'rb')
            data = f.read()
            f.close()
            mime_type = 'image/x-icon'
            body = data
            header = HTTP_RESPONSE_200_OK.format(mime_type)
            conn.send(header.encode())
            conn.send(body)
            conn.close()
    
    # 파일 존재 여부 확인
    if os.path.isfile(filename):
        if filename.endswith('.html'):
            f= open(filename, 'r', encoding='utf-8')
            data = f.read()
            f.close()
            mime_type = 'text/html'
            body = data
            header = HTTP_RESPONSE_200_OK.format(mime_type) 
            conn.send(header.encode())
            conn.send(body.encode('euc-kr'))            #한글 텍스트 파일을 읽어오기 위해 euc-kr로 인코딩
            conn.close()
        elif filename.endswith('.png'):
            f=open(filename, 'rb')
            data = f.read()
            f.close()
            mime_type = 'image/png'
            body = data
            header = HTTP_RESPONSE_200_OK.format(mime_type)
            conn.send(header.encode())
            conn.send(body)
            conn.close()
    else :
        head = HTTP_RESPONSE_404_NOT_FOUND_HEAD
        body = HTTP_RESPONSE_404_NOT_FOUND_BODY
        conn.send(head.encode())
        conn.send(body.encode())
        conn.close()
        break        



