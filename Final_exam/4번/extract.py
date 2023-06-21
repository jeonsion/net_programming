
# 아래 URL에서 이메일 주소를 수집하는 프로그램을 작성하라


import re
import requests


URL = "https://en.wikipedia.org/wiki/Internet_of_things"
rsp = requests.get(URL)
html = rsp.text

iot_list = re.findall(r'([iI][oO][tT]\w+)', html)
print(iot_list)