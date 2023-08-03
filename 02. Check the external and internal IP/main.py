import socket
import requests
import re

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(('www.google.com', 443))
print('internal IP :', in_addr.getsockname()[0])

req = requests.get('http://ipconfig.kr/')
out_addr = re.search(r"IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", req.text)[1]
print('external IP :', out_addr)