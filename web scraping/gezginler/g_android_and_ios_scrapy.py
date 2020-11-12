from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time
###
from util import json_save
def scrapy(key):
    url = "https://www.gezginler.net/android/" + key
    driver = webdriver.Chrome()
    driver.get(url)
    height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == height:
            break
        height = new_height
    time.sleep(1)
    source = driver.page_source
    driver.close()
    bs = soup(source,'html.parser')
    items = {}
    for app in bs.find_all('div',{'class':'masonry-brick'}):
        href = app.find('a').get('href')
        title = app.find('a').strong.text
        title = title.lower().replace(' ','_').replace('-','').replace('!','').replace('ü','u').replace('ç','c').replace('İ','i').replace('ğ','g').replace('ö','o')
        #info = app.find('a')[-1].text
        data = {
            'link':href,
        }
        items[title] = data
    json_save(items, "android-eğitim")
    
if __name__=='__main__':
    # araclar, egitim, eglence, ekonomi, fotograf, haberler, muzik, oyunlar ...
    scrapy("egitim")
    # scrapy("araclar")
    # scrapy("fotograf")
    # scrapy("haberler")
    # scrapy("eglence")
    # scrapy("ekonomi")
