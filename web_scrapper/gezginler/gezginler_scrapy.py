from bs4 import BeautifulSoup as soup
import requests
from gezginler_urls import URL

# s_len = sayfalama.find_all('a')[-2].text
# sayfalama = so.find('div',{'id':'sayfalama'})
class Gezginler:

    def __init__(self):
        self.link = []
        self.name_text = []
        self.info = []
        self.text = []

    # def windows_kategorisi(self):
    #     url = "https://www.gezginler.net/indir/"
    #     req = requests.get(url, timeout=5).content
    #     so = soup(req, 'html.parser')
    #     kategori = so.find('div',{'id':'kategoriler'})
    #     liste = []
    #     for baslik in kategori.find_all('h4'):
    #         liste.append(baslik.text.replace(' & ','-').replace(' - ','-').replace('ü','u').replace('ğ','g').replace('ç','c').lower())
    #         return liste

    #     for i in kategori.find_all('li'):
    #         link = i.a.get('href')
    #         alt_kategori = i.a.text.strip().replace(" - ","-").replace(" / ","-").replace(" ","").replace('ü','u').replace('ğ','g').replace('ç','c').lower()
    #     #    dic[f'{j}'] = {alt_kategori:link}
    #         print(alt_kategori," ",link)

    def scrapy(self,kategory, key):
        a = 1
        start = True
        #########################################################################################
        # URL dosyasında key ve value değerlerinde boşluklar var onların test edilip düzeltilmesi
        # deneme = URL.get('internet')
        # for i in deneme.keys():
        #     print([i.strip()])
        #     print([deneme.get(i).strip()])
        #####################################
        ust_kategori = URL.get(kategory)
        while start != False:
            for i in ust_kategori.keys():
                if key in i.strip():
                    # url = "https://www.gezginler.net/indir/internet/ag-araclari/s/1"
                    url =  ust_kategori.get(i).strip() + 's/{}'.format(str(a))
                    # url = "https://www.gezginler.net/indir/internet/ag-araclari/s/2"
                    #
                    req = requests.get(url, timeout=5).content
                    so = soup(req, 'html.parser')
                    sayfa = so.find('div', {'id': 'sayfalar'})
                    sayfalar = sayfa.find_all('p', {'class': 'list'})

                    # sayfalama, sayfa sayısını bulma ve sayfalama var mı yok mu
                    sayfalama = so.find('div', {'id': 'sayfalama'})
                    if sayfalama.text.strip() != '':
                        s_len = sayfalama.find_all('a')[-2].text #sayfa sayısını bulma
                    else:
                        s_len = 0
                        # -- sayfalama, sayfa sayısını bulma bitiş
                    for i in sayfalar:
                        link = i.find('a', {'class': 'prisim'})
                        span = i.find('span')
                        metin = i.text.replace(i.span.text,'').replace(i.a.text,'').strip()
                        # span = i.find('a',{'span':'basic'})
                        self.link.append(link['href'])
                        self.name_text.append(link.text)
                        self.info.append(span.text.replace(' ','').replace('|','_'))
                        self.text.append(metin) 
                        # print(link.text, " ", link['href'], " ", span.text)
                        # print("--"*40)
                    
                    if str(s_len).strip() != "« Önceki Sayfa":
                        if a < int(s_len):
                            a += 1
                        else:
                            start = False
                    else:
                        start = False
        return list(zip(self.name_text,self.link,self.info,self.text))
    def scrapy_print(self,name1,name2):
        for i in self.scrapy(name1,name2):
            print(i[0]," ",i[1]," ",i[2].replace('_','|'))
            #print(i[3],"\n")

if __name__ == '__main__':

    gezgin = Gezginler()
    gezgin.scrapy_print('araclar', 'optimizasyon')
    #gezgin.scrapy_print('ticari', 'saglik')
    #araclar kategorisi
    #scrapy('araclar', 'diskaracları')
    #scrapy('araclar', 'dosyaaracları')
    #scrapy('araclar', 'dönuşturme-hesaplama')
    #scrapy('araclar', 'kayıtdefteri')
    #scrapy('araclar', 'optimizasyon')
    #scrapy('araclar', 'pdfaracları')
    #scrapy('araclar', 'pratikaraclar')
    #scrapy('araclar', 'sanaldisk-sistem')
    #scrapy('araclar', 'sistemaracları')
    #scrapy('araclar', 'sistembilgisi')
    #scrapy('araclar', 'sistemgereksinimleri')
    #
    #
    #
    # diğer kategorisi
    #gezginler_scrapy('diger', 'unix-linux')
    #

    # ticari kategorisi
    #scrapy('ticari', 'sektorel')
    #scrapy('ticari', 'saglik')
    #scrapy('ticari', 'satis')
    #scrapy('ticari', 'yonetim')

    #internet kategorisi
    #scrapy('internet', 'agaracları')
    #scrapy('internet', 'browser&tarayıcı')
    #scrapy('internet', 'ftp')
    #scrapy('internet', 'hızlandırıcılar')
    #scrapy('internet', 'mail')
    #
    #
    #
    #
    #
    #
    #
