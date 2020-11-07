from bs4 import BeautifulSoup as soup
import requests, zipfile, io
import urllib3
#import re
import json
#
from gezginler_urls import URL
# s_len = sayfalama.find_all('a')[-2].text
# sayfalama = so.find('div',{'id':'sayfalama'})

# def windows_kategorisi(self):
#     url = "https://www.gezginler.net/indir/"
#     req = requests.get(url, timeout=5).content
#     so = soup(req, 'html.parser')
#     kategori = so.find('div',{'id':'kategoriler'})
#     liste = []
#     for baslik in kategori.find_all('h4'):
#         liste.append(baslik.text.replace(' & ','-').replace(' - ','-').replace('ü','u').replace('ğ','g').replace('ç','c').lower())
#     print(liste)

#     for i in kategori.find_all('li'):
#         link = i.a.get('href')
#         alt_kategori = i.a.text.strip().replace(" - ","-").replace(" / ","-").replace(" ","").replace('ü','u').replace('ğ','g').replace('ç','c').lower()
#         dic[f'{j}'] = {alt_kategori:link}
#         print(alt_kategori," ",link)

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
                    #span = i.find('span')
                    # metin = i.text.replace(i.span.text, '').replace(i.a.text, '').strip()
                    # span = i.find('a',{'span':'basic'})
                    l = link['href']
                    #l_t = link.text
                    #span_text = span.text.replace(' ', '').replace('|', '_')
                    links.append(l)
                    # print(link.text, " ", link['href'], " ", span.text)
                if str(s_len).strip() != "« Önceki Sayfa":
                    if a < int(s_len):
                        a += 1
                    else:
                        start = False
                else:
                    start = False
    return links
def app_view_scrapy(name1, name2):
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
            baslik_name: {
                'rating_star': rating_star,
                'rating_oy': [rating_oy.text if rating_oy is not None else '0'][0],
                'img_link': [img_link['src'] if img_link is not None else None][0],
                'download_link': [download.get('onclick')[11:-13] if download is not None else None][0],
            }
        }
        def txt_save():
            with open("data.txt", "+a") as write_file:
                write_file.write(baslik_name + " " + img_link['src'] +'\n')
        ###
        def json_save():
            with open("data_file3.json", "+a") as write_file:
                json.dump(data, write_file)
                write_file.write('\n')
        ###
        def app_download():
            #url = "http://www.magicnotes.com/steelbytes/HD_Speed_ENG_Win32.zip"
            url = download.get('onclick')[11:-13]
            r = requests.get(url,stream=True)
            if download is not None:
                with open(baslik_name+".exe",'wb') as write_file:
                    write_file.write(r.content)
            else:
                with open(baslik_name +".zip",'wb') as write_file:
                    write_file.write(r.content)
        
        ######################       
        # app_download()   
        # json_save()
        # txt_save()
        #####################       
if __name__ == '__main__':
    #app_view_scrapy('araclar', 'diskaracları')
    # scrapy('araclar', 'dosyaaracları')
    # scrapy('araclar', 'dönuşturme-hesaplama')
    #app_view_scrapy('araclar', 'kayıtdefteri')
    #app_view_scrapy('araclar', 'optimizasyon')
    app_view_scrapy('araclar', 'pdfaracları')
    # scrapy('araclar', 'pratikaraclar')
    # scrapy('araclar', 'sanaldisk-sistem')
    # scrapy('araclar', 'sistemaracları')
    app_view_scrapy('araclar', 'sistembilgisi')
    # scrapy('araclar', 'sistemgereksinimleri')
    #
    #
    #
    # diğer kategorisi
    # gezginler_scrapy('diger', 'unix-linux')
    #

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
    #
    #
    #
    #
