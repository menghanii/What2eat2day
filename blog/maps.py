from decouple import config
import requests
import json

# Geocoding을 위한 요청 URL (경도, 위도 구하는)
url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"

# Headers에 넣을 꺼 (Accept, SecretKey 2개)
headers = {'Accept': 'application/json'} 
headers['X-NCP-APIGW-API-KEY-ID'] = config('X-NCP-APIGW-API-KEY-ID')
headers['X-NCP-APIGW-API-KEY'] = config('X-NCP-APIGW-API-KEY')

# Post_detail.html에 넘길 SecretKey
na_id = config('X-NCP-APIGW-API-KEY-ID')
