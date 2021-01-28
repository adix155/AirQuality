from data import *

import ipinfo
import socket
import requests

f = requests.request('GET', 'http://myip.dnsomatic.com')
ip = f.text
print(ip)

access_token = '0cd3132a1d7552'
handler = ipinfo.getHandler(access_token)
details = handler.getDetails(ip)
print(details.loc)
print(details.city)
