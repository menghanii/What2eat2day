import requests
import json

url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"
headers = {'Accept': 'application/json', 'X-NCP-APIGW-API-KEY-ID': 'r1e5o8jg6h', 'X-NCP-APIGW-API-KEY': 'jHsTAMcR2u67EhiqscUtZIkv2qSNnvWATmW1FRUp'}
params = {'query': '서울시 도봉구 방학로15길 40'}
res = requests.get(url, headers=headers, params=params)
temp = res.json()
print(temp)
print(temp['addresses'][0]['x']) #경도
print(temp['addresses'][0]['y']) #위도
