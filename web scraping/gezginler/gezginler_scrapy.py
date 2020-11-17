from bs4 import BeautifulSoup as soup
from selenium import webdriver
import requests
import time
#
from gezginler_urls import URL
from util import json_save
###
def android_and_ios_scrapy(kategori,key, path):
    android = "https://www.gezginler.net/android/"
    ios = "https://www.gezginler.net/ios/"
    if kategori == 'android':
        kategori = android
    elif kategori == 'ios':
        kategori = ios
    else:
        print('Sadece android ve ios kategorisi vardır...')
        return 0
    url =  kategori + key
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
        items[title.replace('ş','s').replace('ı','i')] = href
    json_save(items, path)
###
def windows_kategorisi():
    url = "https://www.gezginler.net/indir/"
    req = requests.get(url, timeout=5).content
    so = soup(req, 'html.parser')
    kategori = so.find('div',{'id':'kategoriler'})
    liste = []
    for baslik in kategori.find_all('h4'):
        liste.append(baslik.text.replace(' & ','-').replace(' - ','-').replace('ü','u').replace('ğ','g').replace('ç','c').lower())
    print(liste)
    for i in kategori.find_all('li'):
        link = i.a.get('href')
        alt_kategori = i.a.text.strip().replace(" - ","-").replace(" / ","-").replace(" ","").replace('ü','u').replace('ğ','g').replace('ç','c').lower()
        dic[f'{j}'] = {alt_kategori:link}
        print(alt_kategori," ",link)
###
def scrapy(kategory, key):
    a = 1
    start = True
    #########################################################################################
    # URL dosyasında key ve value değerlerinde boşluklar var onların test edilip düzeltilmesi
    # deneme = URL.get('internet')
    # for i in deneme.keys():
    #     print([i.strip()])
    #     print([deneme.get(i).strip()])
    #####################################
    links = []
    ust_kategori = URL.get(kategory)
    while start != False:
        for i in ust_kategori.keys():
            if key in i.strip():
                # url = "https://www.gezginler.net/indir/internet/ag-araclari/s/1"
                url = ust_kategori.get(i).strip() + 's/{}'.format(str(a))
                # url = "https://www.gezginler.net/indir/internet/ag-araclari/s/2"
                #
                req = requests.get(url, timeout=5).content
                so = soup(req, 'html.parser')
                sayfa = so.find('div', {'id': 'sayfalar'})
                sayfalar = sayfa.find_all('p', {'class': 'list'})
                # sayfalama, sayfa sayısını bulma ve sayfalama var mı yok mu
                sayfalama = so.find('div', {'id': 'sayfalama'})
                if sayfalama.text.strip() != '':
                    s_len = sayfalama.find_all(
                        'a')[-2].text  # sayfa sayısını bulma
                else:
                    s_len = 0
                    # -- sayfalama, sayfa sayısını bulma bitiş
                for i in sayfalar:
                    link = i.find('a', {'class': 'prisim'})
                    l = link['href']
                    l_t = link.text
                    links.append(l)
                    print(link.text, " ", link['href'], " ")
                if str(s_len).strip() != "« Önceki Sayfa":
                    if a < int(s_len):
                        a += 1
                    else:
                        start = False
                else:
                    start = False
    return links
def app_view_scrapy(name1, name2):
    items = {}
    for link in scrapy(name1, name2):
        url = requests.get(link)
        bs = soup(url.content, 'html.parser')
        ###
        download = bs.find('div', {'id': 'indir'}).find("a", {'itemprop': 'downloadURL'})
        baslik = bs.find('div', {'id': 'baslik'})
        app_information = bs.find('div', {'id': 'detayads'}).find_all('div', {'class': 'dl'})
        ###
        img_link = baslik.find('img', {'itemprop': 'image'})
        baslik_name = baslik.find('span', {'itemprop': 'name'}).text.replace(' ', '_').lower().replace('ı','i')
        rating_info = baslik.find('div', {'class': 'rating'}).find('strong', {'class', 'ratingval'})
        rating_star = rating_info.span.text
        rating_oy = rating_info.find('span', {'itemprop': 'ratingCount'})
        data = {
                #'virus_scan':app_information[7]('span').text, 
                'system':app_information[6]('span')[-1].text,
                'update':app_information[5]('span')[0].text,
                'interface': app_information[4]('span')[0].text.strip().replace('\n','').replace('İ','i').replace('ç','c').replace('I','i').replace('ü','u'),
                'person':app_information[3]('span')[0].text.strip().replace('\n','').replace('ç','c'),
                'size':app_information[2].text[6:].strip().replace('\n',''),
                'license' : app_information[0]('span')[0].text.strip().lower().replace('\n','').replace('Ü','u').replace('ç','c').replace('ü','u'),
                'publisher' : app_information[1]('span')[0].text.lower(),
                'rating_star': rating_star,
                'rating': [rating_oy.text if rating_oy is not None else '0'][0],
                'img_link': [img_link['src'] if img_link is not None else None][0],
                'download_link': [download.get('onclick')[11:-13] if download is not None else None][0],
        }
        items[baslik_name] = data
    json_save(items,"unix-linux")
    return items
if __name__ == '__main__':
    # Windows uygulamaları kategorisi
    ### uygulamanın içerik bilgilerini almak için app_view_scrapy fonksiyonu çalıştırılmalı
    #app_view_scrapy('araclar', 'diskaracları')
    #app_view_scrapy('araclar', 'optimizasyon')

    #app_view_scrapy('araclar', 'pdfaracları')
    # scrapy('araclar', 'pratikaraclar')
    # scrapy('araclar', 'sanaldisk-sistem')
    # scrapy('araclar', 'sistemaracları')
    # app_view_scrapy('araclar', 'sistembilgisi')
    # scrapy('araclar', 'sistemgereksinimleri')

    # ticari kategorisi
    #app_view_scrapy('ticari', 'sektorel')
    # scrapy('ticari', 'saglik')
    # scrapy('ticari', 'satis')
    # scrapy('ticari', 'yonetim')

    # internet kategorisi
    # scrapy('internet', 'agaracları')
    # scrapy('internet', 'browser&tarayıcı')
    # scrapy('internet', 'ftp')
    # scrapy('internet', 'hızlandırıcılar')
    # scrapy('internet', 'mail')
    #
    #
    #
    # android ve ios uygulamaları kategorisi
    ## araclar, egitim, eglence, ekonomi, fotograf, haberler, muzik, oyunlar ...
    # birinci parametre: ana kategori , ikincisi uygulama kategorisi, diğeri ise kaydedilecek json dosyasınn ismi
    #android_and_ios_scrapy('ios','oyunlar','ios oyunları')
    # android_and_ios_scrapy('android','ekonomi','android_ekonomi')
    # android_and_ios_scrapy('fotograf')
    # android_and_ios_scrapy('muzik')
    #
    #
