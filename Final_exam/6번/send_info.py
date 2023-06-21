import json
import requests

dict_data = {'ID' : '20191545', 'Name' : 'SionJeon', 'Department' :
    'iot'}


url = 'http://httpbin.org/post'
rsp = requests.post(url, json=dict_data)
print(rsp.text)

# json 필드만 추출하기
rsp_dict = json.loads(rsp.text)
print(rsp_dict['json'])