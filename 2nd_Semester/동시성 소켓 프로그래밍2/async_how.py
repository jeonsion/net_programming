import asyncio, time

async def add(a,b):
    print('In add() func')
    await asyncio.sleep(1)
    print(a+b)

async def mul(a,b):
    print('In mul() func')
    await asyncio.sleep(2)
    print(a* b)

async def sub(a,b):
    print('In mul() func')
    await asyncio.sleep(3)
    print(a-b)
    
async def main():
    print(f"started at {time.strftime('%X')}")
    # task1 = asyncio.create_task(add(1,2))
    # task2 = asyncio.create_task(mul(3,4))
    # task3 = asyncio.create_task(sub(5,6))
    # await task1
    # await task2
    # await task3
    
    await asyncio.gather(add(1,2), mul(3,4), sub(5, 6))
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())