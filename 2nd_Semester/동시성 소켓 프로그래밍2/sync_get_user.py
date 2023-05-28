# 사용자가 외부 서버에 저장되어 있다고 가정
# 외부 서버에서 정보를 가져오는데 1초의 시간이 걸린다고 가정

import time

def get_user(name):
    print('사용자 {!r} 정보 조회중...'.format(name))
    time.sleep(1)
    print('사용자 {!r} 정보 조회 완료!!'.format(name))

def main():
    start = time.time()
    get_user('Jeon')
    get_user('Yun')
    get_user('Kim')
    get_user('Song')
    end = time.time()
    print(f"총 소요 시간 : {end - start}")

main()