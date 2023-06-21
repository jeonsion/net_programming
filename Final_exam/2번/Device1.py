#명령어 인자를 통하여 클라이언트가 서버에 접속할 수 있고, 서버로 메시지를 보낼 수 있도록 한다.


from socket import *
import argparse
import random
import time

s = socket(AF_INET, SOCK_STREAM)
parser = argparse.ArgumentParser()
parser.add_argument('-s', default='localhost')
parser.add_argument('-p', type=int, default=2550)
args = parser.parse_args()

s.connect((args.s, args.p))
print('connected to ', args.s, args.p)

while True:
    id = input("Input ID : ")
    if msg == 'q':
        break
    while True:
        #5초마다 1~40사이의 값을 생성한다.
        time.sleep(5)
        value = str(random.randint(1, 40))
        num = ["{} {}".format(id, value)]
        s.send(num.encode())

    
s.close()