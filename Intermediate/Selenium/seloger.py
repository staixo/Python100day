from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import ssl
import requests
from urllib.request import urlopen, Request

url = "https://www.seloger.com/list.htm?projects=2,5&types=1&natures=1,2,4&places=[{%22inseeCodes%22:[750111]},{%22inseeCodes%22:[750112]},{%22inseeCodes%22:[750110]},{%22inseeCodes%22:[750120]},{%22inseeCodes%22:[750104]},{%22inseeCodes%22:[750102]},{%22inseeCodes%22:[750103]}]&price=NaN/350000&surface=20/NaN&rooms=1,2&mandatorycommodities=0&enterprise=0&groundfloor=0&qsVersion=1.0&m=search_refine-redirection-search_results"
ssl._create_default_https_context = ssl._create_unverified_context
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urlopen(req) as response:
    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all('a'):
        try:
            if int(anchor.get_text().split('.')[0]) > 0:
                print(anchor.get_text().split('.')[1])
        except ValueError:
            continue