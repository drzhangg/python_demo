import requests


url = 'http://47.103.9.218'

r = requests.get(url)
html = r.text
print(html)

r.request