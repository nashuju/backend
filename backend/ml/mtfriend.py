# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import json
import requests
url='https://s.taobao.com/list?data-key=s,ps&data-value=0,1&ajax=true&_ksTS=1515936599673_2416&spm=a217f.8051907.312344.14.57b694c0WP9Jpr&q=%E4%B8%AD%E9%95%BF%E6%AC%BE%E6%A3%89%E6%9C%8D&cat=16&style=grid&seller_type=taobao&bcoffset=12&smToken=0c5b0dbe5dbf4de08d704385ef82842f&smSign=8PgXDXfeRsUU2M8JxAwYDA==&s=60'
a=requests.get(url)
print a.text
pass