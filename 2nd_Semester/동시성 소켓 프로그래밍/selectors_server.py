import selectors
import socket

sel = selectors.DefaultSelector() #이벤트 처리기(셀렉터) 객체를 생성한다.

def accept(sock, mask): #연결을 처리 함수
    conn, addr = sock.accept()
    print('Connected from ', addr)
    sel.register(conn, selectors.EVENT_READ, read)  # 클라이언트 소켓을 이벤트 처리기에 등록
    
def read(conn, mask):
    data = conn.recv(1024)
    if not data:
        sel.unregister(conn) #연결을 해제한다.
        conn.close()
        return
    print('Received: ', data.decode())
    conn.send(data)
    
sock = socket.socket()
sock.bind(('localhost', 5021))
sock.listen(5)

sel.register(sock, selectors.EVENT_READ, accept) #서버 소켓을 이벤트 처리기에 등록
while True:
    events = sel.select() #등록된 소켓들에 대하여 이벤트를 감시한다.
    print(events)
    for key, mask in events:
        callback = key.data #이벤트 처리기에 등록된 함수를 호출한다.
        callback(key.fileobj, mask)
        
     
# selectors.DefaultSelector()를 사용하여 이벤트 처리기 (셀렉터) 객체를 생성합니다.
# accept() 함수는 연결을 처리하는 함수입니다. sock.accept()를 통해 클라이언트의 연결 요청을 받으면 소켓을 받아들이고, 해당 클라이언트 소켓을 이벤트 처리기에 등록합니다.
# read() 함수는 데이터를 읽는 함수입니다. conn.recv(1024)를 통해 클라이언트로부터 데이터를 받으면 데이터를 출력하고, 클라이언트에게 다시 데이터를 전송합니다.
# 서버 소켓을 생성하고, 해당 소켓을 이벤트 처리기에 등록합니다. 이벤트 타입은 selectors.EVENT_READ로 설정하여 소켓의 읽기 이벤트를 처리할 수 있도록 합니다.
# sel.select()를 사용하여 등록된 소켓들에 대한 이벤트를 감시합니다. 이 함수는 블로킹되어 이벤트가 발생할 때까지 기다립니다.
# 이벤트가 발생한 소켓들에 대해 등록된 콜백 함수를 호출하여 이벤트를 처리합니다. key 객체에서 소켓과 이벤트 타입을 가져와서 해당 콜백 함수를 호출합니다.
