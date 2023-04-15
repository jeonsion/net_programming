import socket

UDP_IP = "localhost"
UDP_PORT = 5007

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Enter command: ")
    sock.sendto(message.encode(), (UDP_IP, UDP_PORT))

    data, addr = sock.recvfrom(1024)
    response = data.decode()
    if response == "quit":
        break
    print(response)

sock.close()
