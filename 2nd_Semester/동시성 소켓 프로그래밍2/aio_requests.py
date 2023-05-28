import asyncio
import time
import aiohttp

async def download_site(session, url):
    async with session.get(url) as response:
        print(f"Read {response.content_length} from {url}")
        
async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            # download_site 함수를 실행하고, 결과를 tasks에 저장한다.
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)
    
if __name__ == "__main__":
    sites = [
        "https://home.sch.ac.kr/iot",
        "https://home.sch.ac.kr/bigdata"
    ]*80
    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
    
#Downloaded 160 in 0.6098029613494873 seconds