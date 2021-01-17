# -*- coding: utf-8 -*-

# 爬取i问财搜索答案

import pandas as pd
from bs4 import  BeautifulSoup
import re
import urllib.request
import numpy as np
import datetime
import time
import pandas


See Reference: 
https://www.zhihu.com/question/269091574  
https://www.zhihu.com/column/p/26079709 


def get_url(url):
    """
    return soap
    """
    # 加入UserAgent信息，还必须要定期更新cookie中的v信息才能顺利爬取: https://www.zhihu.com/question/269091574
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Cookie':'cid=caa16b9488e51156d0cce0c295a370d61610022122; ComputerID=caa16b9488e51156d0cce0c295a370d61610022122; PHPSESSID=caa16b9488e51156d0cce0c295a370d6; v=A-L3zi4RycoVrNWWgQuvol_MM2lFM-ZNmDfacSx7DtUA_4zbFMM2XWjHKov_',}  

    req = urllib.request.Request(url=url, headers=headers)
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, features = "lxml")   # 用BeautifulSoup解析html
    return soup


if __name__ == '__main__':

    # URLs：涨停溢价指数（883900），炸板负溢价指数（883918），跌停数量指数，首板数量指数（883979），炸板率指数
    pos_premium_html = "http://www.iwencai.com/stockpick/search?typed=1&preParams=&ts=1&f=3&qs=result_rewrite&selfsectsn=&querytype=stock&searchfilter=&tid=stockpick&w=883900&queryarea="
    neg_premium_html = "http://www.iwencai.com/stockpick/search?typed=1&preParams=&ts=1&f=1&qs=result_rewrite&selfsectsn=&querytype=stock&searchfilter=&tid=stockpick&w=883918"
    down_num_html = "http://www.iwencai.com/stockpick/search?typed=1&preParams=&ts=1&f=1&qs=index_rewrite&selfsectsn=&querytype=stock&searchfilter=&tid=stockpick&w=%E8%B7%8C%E5%81%9C%E4%B8%AA%E6%95%B0"
    up1_num_html = "http://www.iwencai.com/stockpick/search?typed=0&preParams=&ts=1&f=1&qs=result_original&selfsectsn=&querytype=stock&searchfilter=&tid=stockpick&w=883979"

    # 涨停溢价
    n = 0
    while 1:
        soup = get_url(pos_premium_html) 
        pick = soup.find(id="doctorPick")
        if pick:
            break
        print(f"try: {n}"); time.sleep(0.2)
        n += 1
    pos_premium = float(pick.find("div", attrs={'class':"em green _x_ alignRight alignRight"}).text)
    print(pos_premium)

    # 炸板负溢价指数
    n = 0
    while 1:
        soup = get_url(neg_premium_html) 
        pick = soup.find(id="doctorPick")
        if pick:
            break
        print(f"try: {n}"); time.sleep(0.2)
        n += 1
    neg_premium = float(pick.find("div", attrs={'class':"em green _x_ alignRight alignRight"}).text)
    print(neg_premium)

    # 跌停数量指数    
    n = 0
    while 1:
        soup = get_url(down_num_html) 
        pick = soup.find(id="table_top_bar")
        if pick:
            break
        print(f"try: {n}"); time.sleep(0.2)
        n += 1
    down_num = float(pick.find("span", attrs={'class':"num"}).text)
    print(down_num)

    # 首板数量
    n = 0
    while 1:
        soup = get_url(up1_num_html) 
        pick = soup.find_all(id="doctorPick")
        print(pick)
        if pick:
            break
        print(f"try: {n}"); time.sleep(0.2)
        n += 1
    up1_num = float(pick.find("span", attrs={'class':"num"}).text)
    print(up1_num)
