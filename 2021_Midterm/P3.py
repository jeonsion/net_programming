str = 'https://search.naver.com/search.naver?where=nexearch&ie=utf8&query=iot'
dict = {}
str = str.split('?')[-1]
for i in str.split("&"):
    key, value = i.split("=")
    dict[key] = value
print(dict)