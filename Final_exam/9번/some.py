#썸네일 생성API를 이용하여 중요한 부분을 썸네일로 생성해보자
#width가 200, height가 200d으로 요청했을 때, 생성된 썸네일을 화면에 출력하자


import requests, json, io

from PIL import Image
from io import BytesIO




REST_API_KEY = "5de868eb7ba5636ff5feb34abe0dad69"

def crop(image_url):
    r  = requests.post(
        'https://dapi.kakao.com/v2/vision/thumbnail/crop',
        json = {
            'Parameter' :{
                'width' : 200,
                'height' : 200
            }
        },
    headers = {'Authorization' : f'KakaoAK {REST_API_KEY}',
               'Content-Type'  : 'application/x-www-form-urlencoded'}
    )
    response = json.loads(r.content)
    return response

def show_some(image_url):
    
    #이미지를 불러온다
    image_rsp = requests.get(image_url)
    file_jpgdata = BytesIO(image_rsp.content)
    image = Image.open(file_jpgdata)
    
    return image


if __name__ == "__main__":
    IMAGE_URL = 'https://t1.daumcdn.net/alvolo/_vision/openapi/r2/images/07.jpg'
    generate_result = crop(IMAGE_URL)
    image = show_some(IMAGE_URL)
    image.show()