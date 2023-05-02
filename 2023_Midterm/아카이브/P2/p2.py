url = "https://search.daum.net/search?w=tot&q=bigdata"
dict = {}

url = url.split("?")[1]
for i in url.split("&"):
    dict[i.split("=")[0]] = i.split("=")[1]
print(dict)
dict['q'] = "iot"
print(dict)
