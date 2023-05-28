# 코루틴 내에서 일반 함수 사용하기
# asyncio.to_thread()함수는 스레드를 이용하여 병렬로 실행함

import asyncio, time

async def get_user(name):
    print('사용자 {!r} 정보 조회중...'.format(name))
    await asyncio.to_thread(time.sleep, 1)
    print('사용자 {!r} 정보 조회 완료!!'.format(name))

async def main():
    start = time.time()
    await asyncio.gather(
    get_user('Jeon'),
    get_user('Yun'),
    get_user('Kim'),
    get_user('Song')
    )
    end = time.time()
    print(f"총 소요 시간 : {end - start}")
    
asyncio.run(main())