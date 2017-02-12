#!/usr/bin/python3
import json
from grab import Grab, UploadFile

URL = "https://geekbrains.ru/api/v2/lessons/3107/homeworks"

f = open("fakeuser.json")
cred = json.loads(f.read())
print(cred['user'], cred['password'])

g = Grab()
g.setup(connect_timeout=20, timeout=20)

print("auth")
g.go('https://geekbrains.ru/login')
g.doc.set_input_by_id('user_email', cred['user'])
g.doc.set_input_by_id('user_password', cred['password'])
g.submit()

print('submit')
g.go(url=URL, multipart_post={'data[attachment]': UploadFile('les1.py')})
g.request()

print(g.response.code)
