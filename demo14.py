#!/usr/bin/env python

# -*- coding: utf-8 -*-

import requests

import re

from bs4 import BeautifulSoup

url ="https://so.csdn.net/so/search/s.do"

p =0

# s = input()

s ='python'

for pin in range(10):
    p = p+1

    kv = {'p':'%d' % p, 'q':'%s' % s}

r = requests.get(url, params=kv)

r.encoding ='utf-8'

    so_url = r.request.url

html = r.text

# print(requests.get(so_url).text)

    soup = BeautifulSoup(html, "html.parser")

for dlin soup.find_all('dl'):

text = dl.prettify()

        search_url = dl.get('data-track-view')

search = re.findall(r'"con":"(.*?)"', search_url)[0]

content = requests.get(search).text

# print(content)

tittle = re.findall(r'<div class="limit_width">\n.*?<a.*?>(.*?)</a>\n.*?<a', text, re.S)[0]

tittle = tittle.replace('<em>', '')

tittle = tittle.replace('</em>', '')

tittle = tittle.replace(' ', '')

tittle = tittle.replace('\n', '')

fb =open('%s.html' % tittle, 'w', encoding='utf-8')

fb.write(content)

print(search, tittle)

#exit()

# print(search)

作者：MySuperHero
链接：https://www.jianshu.com/p/757d8981fdda
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。