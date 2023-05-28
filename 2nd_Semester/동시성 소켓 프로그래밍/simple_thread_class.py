#파이썬 멀티스레드 방법 2 - Thread 클래스를 상속받아서 구현하는 방법
#Thread 클래스를 상속받아서 run() 메소드를 오버라이딩하고,
#run() 메소드에서 스레드가 실행할 코드를 작성한다.
#start() 메소드를 호출하면 run() 메소드가 호출되면서 스레드가 실행된다.
#join() 메소드를 호출하면 해당 스레드가 종료될 때까지 기다린다.

import threading
import datetime

class myThread(threading. Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.name = name
        self.counter = counter
    
    
    #run() 메소드에서 스레드가 실행할 코드를 작성한다.
    def run(self):
        print("\nStarting {} [{}]".format(self.name, self.counter))
        print_date(self.name, self.counter)
        print('Exiting {} [{}]' + self.name, self.counter)
        
def print_date(threadName, counter):
    today = datetime.date.today()
    print('\n{} [{}] : {}'.format(threadName, counter, today))
        
#스래드 객체를 생성한다.
thread1 = myThread('Thread', 1)
thread2 = myThread('Thread', 2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print('\nExiting the program')