# coding=utf-8
import requests

url = "http://localhost:5001/upload"
file = open("test.mp4", 'rb')
files = {'file': file}

r = requests.post(url, files=files)

file.close()

print(r.text)

