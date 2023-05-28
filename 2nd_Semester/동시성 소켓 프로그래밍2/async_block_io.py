import asyncio, time

def blocking_io(): #일반함수 선언
    print(f"Start blocking_io at {time.strftime('%X')}")
    time.sleep(1)
    print(f"blocking_io complete at {time.strftime('%X')}")

async def main():
    print(f"Start main at {time.strftime('%X')}")
    await asyncio.gather(
        asyncio.to_thread(blocking_io),
        asyncio.sleep(1)
    )
    
asyncio.run(main())