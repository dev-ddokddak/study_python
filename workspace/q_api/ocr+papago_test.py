import os
import sys
import urllib.request
import json

# K89972633688957
# https://ocr.space/OCRAPI
import requests
import json

url = "https://api.ocr.space/parse/imageurl?apikey=K89972633688957&url=https://hanasia.com/_sys/_upload/image/201906/12/15603238171847.jpg&language=kor&isOverlayRequired=true"

response = requests.get(url)
response.raise_for_status()

data = response.json()
print(data['ParsedResults'][0]['ParsedText'])

# print(json.dumps(data, ensure_ascii=False, indent=2))



client_id = "NtrbPbnlVHbZlrkrIV_9" # 개발자센터에서 발급받은 Client ID 값
client_secret = "M4KwjY5Mor" # 개발자센터에서 발급받은 Client Secret 값
encText = urllib.parse.quote(data['ParsedResults'][0]['ParsedText'])
data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode == 200): # 200이라는 코드는 성공코드
    response_body = response.read()
    # 받은 데이터는 json이다
    print(response_body.decode('utf-8'))
    # json.loads(json)을 사용하여 dict로 변환한다.
    print(json.loads(response_body.decod('utf-8'))["message"]["result"]["translatedText"])
else:
    print("Error Code:" + rescode)