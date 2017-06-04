# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 18:10:08 2017

@author: AutuanLiu
"""

import requests
from bs4 import BeautifulSoup
import re
sum = 0
r = requests.get('https://book.douban.com/subject/27038949/comments/')
soup = BeautifulSoup(r.text, 'lxml')
pattern = soup.find_all('p', 'comment-content')
for item in pattern:
    print(item.string)
    pattern_s = re.compile('<span class="user-stars allstar(.*) rating"')
    p = re.findall(pattern_s, r.text)
for star in p:
    sum += int(star)
    print(sum)
    
