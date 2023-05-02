import socket

ip = "220.69.189.125"
port = 443
ip_data = list(socket.gethostbyaddr(ip))
#print(ip_data) # 결과 : '[home.sch.ac.kr', ['125.189.69.220.in-addr.arpa'], ['220.69.189.125']
#IP 주소으의 호스트 네임 출력
print(ip_data[0])

#포트번호 443에 해당하는 프로토콜 출력
print(socket.getservbyport(port))
protocol = socket.getservbyport(port)

print("{}://{}".format(protocol, ip_data[0]))
packed_ip = socket.inet_aton(ip)
print(packed_ip)