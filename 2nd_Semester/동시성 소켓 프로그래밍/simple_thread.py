#파이썬 멀티스레드 구현 방법 1 - threading 모듈을 이용한 구현 방법 
#스레드 객체를 생성하고 start() 메소드를 호출하면 스레드가 실행된다.

import threading

def prtSquare(num):
    print("Square: {}".format(num**2))

def prtCube(num):
    print("Cube: {}".format(num**3))


#모듈을 이용하여 함수를 스레드로 실행하는 방법, 함수를 인자로 넘겨준다.
t1 = threading.Thread(target = prtSquare, args = (10,))
t2 = threading.Thread(target = prtCube, args = (10,))

t1.start()
t2.start()

t1.join()
t2.join()

print('Done')