import socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = ''
Port = 9003

s.bind((IP, Port))
s.listen()

while True :
    client, addr = s.accept()
    print('Connection from ', addr )
    client.send(b'Hello' + addr[0].encode())
    msg = client.recv(1024)
    print(msg.decode())
    
    StudentNum = 20191545
    #int.to_bytes()는 4바이트를 보내야함
    client.send(StudentNum.to_bytes(4, 'big')) 
    client.close()

    
    