# Python - Network #1
This project will help out to test the usage of python important module called requests as well as urllib
# Installation
python -m pip install requests

# Usage of Requets
>>> import requests

>>> r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))

>>> r.status_code

200

>>> r.headers['content-type']

'application/json; charset=utf8'

>>> r.encoding

'utf-8'

>>> r.text

'{"authenticated": true, ...'

>>> r.json()

{'authenticated': True, ...}
# usage of urllib
import urllib.request

req = urllib.request.Request('http://python.org/')

with urllib.request.urlopen(req) as response:
   
	the_page = response.read()
