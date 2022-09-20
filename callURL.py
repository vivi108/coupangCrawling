from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
import requests
import re
import pandas as pd
import numpy as np
import os
from fake_useragent import UserAgent
from user_agent import generate_user_agent, generate_navigator

# Headers 원래 필수 값이 아니다. 하지만 쿠팡의 경우 headers 없이 크롤링 했을때는 결과가 한개도 나오지 않는다.
# 그래서 headers를 위와 같이 설정해주면 된다



def getPageString(url):
    # ua = UserAgent(verify_ssl=False, use_cache_server=True)
    # userAgent=ua.random
    userAgent =generate_user_agent(device_type='desktop')
    header = {
        'User-Agent': userAgent}
    print(userAgent)
    data = requests.get(url, headers=header)
    return data.content


getPageString("https://www.coupang.com/np/categories/497135")