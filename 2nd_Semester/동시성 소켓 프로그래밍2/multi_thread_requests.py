import concurrent.futures
import requests, threading, time

thread_local = threading.local()

def get_session():
    
    # thread_local에 session이 없으면
    # hasattr   :   객체에 해당 속성이 있는지 확인, 있으면 True, 없으면 False 
    if not hasattr(thread_local, "session"):    
        thread_local.session = requests.Session()
    return thread_local.session

def download_site(url):
    seesion = get_session()
    with seesion.get(url) as response:
        print(f"Read {len(response.content)} from {url}")

def download_all_sites(sites):
    # max_workers=5 : 최대 5개의 스레드를 사용한다.
    #스레드 풀을 사용하면 스레드를 생성하고, 스레드를 종료하는 과정을 자동으로 처리한다.
    #executor은 스레드 풀 객체
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor: 
        executor.map(download_site, sites)
        
if __name__ == "__main__":
    sites = [
        "https://home.sch.ac.kr/iot",
        "https://home.sch.ac.kr/bigdata"
    ]*80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")


#Downloaded 160 in 1.5813801288604736 seconds