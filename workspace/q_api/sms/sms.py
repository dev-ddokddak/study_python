import json
import platform
import requests
import config
import auth


default_agent = {
    'sdkVersion': 'python/4.2.0',
    'osPlatform': platform.platform() + " | " + platform.python_version()
}


url = "http://api.coolsms.co.kr/messages/v4/send"
headers = auth.get_headers('NCSQWUG6EB8ZQ176', 'A1XZ0UE8TBG5NSNVAN0DHG4TCTUBPZW5')

data = {
    "message": {
        "to": "01072970766",
        "from": "01072970766",
        "text": "인증번호 : 121212"
    }
}
print(json.dumps(data, ensure_ascii=False))
response = requests.post(config.get_url('/messages/v4/send'),
                         headers=auth.get_headers(config.api_key, config.api_secret),
                         json=data)
print(response.status_code)
print(response.text)
