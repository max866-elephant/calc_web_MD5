# -*- coding:utf-8 -*-
# Taiwan No.1
# first modify urls.txt for wanna to check web url
# python app.py 

import requests
from datetime import datetime, timezone, timedelta
from bs4 import BeautifulSoup
import hashlib
import time
from datetime import datetime

urls = []
try:
  with open('urls.txt','r') as f:
    urls = [line.rstrip() for line in f]
except:
  print('read urls.txt Error')


def main():
    global urls

    for url in urls:
      try:
        res = requests.get(url)
        content = BeautifulSoup(res.text, 'html.parser')
        m = hashlib.md5()
        m.update(content.encode('utf-8'))
        h = m.hexdigest()
        print(f'{url} hash : {h}')
      except Exception as e:
        print('request url or check hash Error!')
        # print(e)

if __name__ == '__main__':
    while True:
        print(datetime.now())
        main()
        print('-'*30)
        time.sleep(10)