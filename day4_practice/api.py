import requests, json

url = 'http://127.0.0.1:8000/'

data = requests.get(url=url)
print(data.json())