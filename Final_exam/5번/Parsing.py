from urllib import parse
import requests

url = 'https://search.naver.com/search.naver?query=iot'
result = parse.urlparse(url)
print(result)

new_url = parse.urlunparse(result[:4] + ('', ''))
print(new_url)


rsp = requests.get(new_url)
payload = {'query': 'iot'}
rsp = requests.get(url, params=payload)
print(rsp.headers)
