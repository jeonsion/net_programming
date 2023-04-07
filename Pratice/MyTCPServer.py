class TCPServer:
    def __init__(self, port):
        import socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('', port))
        self.sock.listen()
        
    def Accept(self):
        self.c_sock, self.c_addr = self.sock.accept()
        return self.c_sock, self.c_addr
    
if __name__ == '__name__':
    sock = TCPServer(5000)
    c, addr = sock.Accept()
    print('conneted by ', addr)
    c.send(b'Hello Client')
    c.close()