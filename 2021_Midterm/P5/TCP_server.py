from socket import *



port = 2503
BUFSIZ = 1024
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen()

conn, addr = sock.accept()


dict = {}
while True:
    data = conn.recv(BUFSIZ)
    data = data.decode()
    if data == "quit":
        break
    
    split_data = data.split()
    type = split_data[0]
    mboxId = split_data[1]
    message = " ".join(split_data[2:])
    
   
    if type == "send":
        if mboxId in dict:
            dict[mboxId].append(message)
        else:
            dict[mboxId] = [message]    #리스트형태로 [message]를 넣어줘야하는게 중요!!!!
        conn.send("OK".encode())
    elif type == "receive":
        if mboxId in dict:
            if len(dict[mboxId]) > 0 :
                send_message = dict[mboxId][0]
                del dict[mboxId][0]
                conn.send(send_message.encode())
            else:
                conn.send("No message".encode())
        else:
            conn.send("No message".encode())
conn.close()
                