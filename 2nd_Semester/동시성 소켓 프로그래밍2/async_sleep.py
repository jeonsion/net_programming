import asyncio, time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
    
async def main():
    print(f"started at {time.strftime('%X')}")
    
    task1 = asyncio.create_task(    # asyncio.create_task()는 say_after()를 실행한다.
        say_after(1, 'hello'))
    task2 = asyncio.create_task(   # asyncio.create_task()는 say_after()를 실행한다.
        say_after(2, 'world'))
    
    await task1 # await: task1이 끝날 때까지 기다린다.
    await task2 # await: task2가 끝날 때까지 기다린다. 
    
    print(f"finshed at {time.strftime('%X')}")
    
asyncio.run(main()) # asyncio.run()은 main()을 실행한다.