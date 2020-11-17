from requests_html import HTMLSession
from bs4 import BeautifulSoup
import re
import time
import json
#
from util import json_save
#
URL = {
    'pc':'https://www.hepsiburada.com/bilgisayarlar-c-2147483646',
    'elektronik':'https://www.hepsiburada.com/ev-elektronik-urunleri-c-2147483638',
    'tel':'https://www.hepsiburada.com/telefonlar-c-2147483642',
    'cep_tel':'https://www.hepsiburada.com/cep-telefonlari-c-371965',
    'beyazesya':'https://www.hepsiburada.com/beyaz-esya-mutfak-urunleri-c-2147483637',
    'foto':'https://www.hepsiburada.com/foto-kameralari-c-2147483606',
    'spor':'https://www.hepsiburada.com/spor-outdoor-urunleri-c-60001546',
    'giyim':'https://www.hepsiburada.com/giyim-ayakkabi-c-2147483636',
    'taki':'https://www.hepsiburada.com/altin-taki-mucevherler-c-2147483617',
    'aksesuar':'https://www.hepsiburada.com/saat-gozluk-aksesuarlari-c-2147483632',
    'kozmetik':'https://www.hepsiburada.com/kozmetik-c-2147483603',
    'oyuncak':'https://www.hepsiburada.com/anne-bebek-oyuncak-c-2147483639',
    'oyuncaklar':'https://www.hepsiburada.com/oyuncaklar-c-23031884',
    'film_muzik_kitap':'https://www.hepsiburada.com/kitaplar-filmler-muzikler-c-60001501',
    'hobi_oyun':'https://www.hepsiburada.com/hobi-oyun-konsollari-c-60003054',
    'ofis_kırtasiye':'https://www.hepsiburada.com/kirtasiye-ofis-urunleri-c-2147483643',
    'market_bahce_yapi':'https://www.hepsiburada.com/yapi-market-bahce-oto-c-60002705',
    'oto':'https://www.hepsiburada.com/oto-lastikler-c-259720',
    'ev':'https://www.hepsiburada.com/ev-dekorasyon-c-60002028',
    'mobilya':'https://www.hepsiburada.com/mobilyalar-c-18021299',
    'pet_shop':'https://www.hepsiburada.com/pet-shop-c-2147483616',
    'super_market':'https://www.hepsiburada.com/supermarket-c-2147483619',
    'duvar_kagitlari':'https://www.hepsiburada.com/duvar-kagitlari-c-18042736',
    'hesap_makinesi':'https://www.hepsiburada.com/casio/hesap-makineleri-c-15298',
    'tv':'https://www.hepsiburada.com/led-tv-televizyonlar-c-163192',
    'parfum':'https://www.hepsiburada.com/parfumler-c-341406',
    'bebek_arabalari':'https://www.hepsiburada.com/bebek-arabalari-c-60002064',
    'bebek_bezi':'https://www.hepsiburada.com/bebek-bezi-c-60001048',
}
####################################################################################################3
# def kategori_linkleri():
#     session = HTMLSession()
#     r = session.get('https://www.hepsiburada.com/')
#     soup = BeautifulSoup(r.html.html,'html.parser')
#     for i in soup.find('div',class_ = 'footer-middle-left')('section')[1]('a'):
#         print(i.get('href'))
def tum_kategori_linkleri():
    session = HTMLSession()
    r = session.get('https://www.hepsiburada.com/tum-kategoriler')
    soup = BeautifulSoup(r.html.html,'html.parser')
    a = 0
    items = {}
    while True:
        try:
            container = soup.find_all('div', class_='categories')
            group = container[a].find_all('div',class_='group')
            for i in group:
                anabaslik = i.find('a')
                if anabaslik is not None:
                    it = {}
                    for j in i('a'):
                        baslik = j.text.lower().replace('&','').replace(' ','').replace('/','').replace('ö','o').replace('ü','u')
                        link = "https://www.hepsiburada.com" + str(j.get('href'))
                        it[baslik] = link
                    items[anabaslik.text.lower().replace('.','').replace('/','')] = it     
            a += 1
        except:
            break
    json_save(items,'tüm_kategoriler')
####################################################################################################3
def hepsiburada_linkleri(key):
    session = HTMLSession()
    liste = []
    pattern = re.compile(r'p-[a-zA-Z]{1,}[0-9]{1,}[a-zA-Z0-9]{1,}') # regex şablonumuz # p-HBV00000Y8E0O
    ###############################3 
    req = session.get(URL[key])
    soup = BeautifulSoup(req.html.html,'html.parser')
    sayfalama = soup.find('div',{'id':'pagination'})('li')[-1].text.strip()
    ####################################
    for a in range(1,int(sayfalama)):
        try:
            url = URL[key] + "?sayfa={}".format(a)
            req = session.get(url)
            time.sleep(1.5)
            container = req.html.find('.product-list')[0]
            for i in container.absolute_links: # tüm linkler , all links
                r = re.search(pattern,i)
                if r is not None:
                    urun_kimligi = r.group() # çıktı, output, example: p-HBV00000Y8E0O
                    liste.append(urun_kimligi)
        except:
            break
    json_save(liste, key)
###
def urun_icerigi(path, key):
    session = HTMLSession()
    with open(path +'.json','r') as f:
        u_kimlikler = json.load(f)
        for u_kimlik in u_kimlikler:
            # Url linklerindeki c-60001048 kısımlarını json dosyasından gelecek kimlik ile değiştiriyoruz
            url = URL[key].replace(re.search(r'c-[0-9]{1,}',URL[key]).group(), u_kimlik)
            r = session.get(url)
            time.sleep(1.5)
            try:
                isim = r.html.find('.product-name')[0].text
                orgfiyat = r.html.find('#originalPrice')[0].text
                fiyat= r.html.find('.extra-discount-price')[0].text
                indirim = r.html.find('.discount-amount')[0].text
            except : 
                isim = "None"
                orgfiyat = 'None'
                fiyat = "None"
                indirim = 'None'
            print("HB: ",isim," ---> ", fiyat,"eski fiyatı: "+orgfiyat, indirim+" indirim")

if __name__ =='__main__':
    ### urun kimliklerini kaydetmek için hepsiburada_linkleri() çalıştırılmalı
    # hepsiburada_linkleri('oto')
    # hepsiburada_linkleri('elektronik')
    # hepsiburada_linkleri('duvar_kagitlari')
    # hepsiburada_linkleri('parfum')
    #hepsiburada_linkleri('aksesuar')
    #hepsiburada_linkleri('super_market')
    #hepsiburada_linkleri('cep_tel')
    
    ### urun içeriklerini görüntülemek için json dosyasına ihtiyaç vardır
    #urun_icerigi('oto','oto')
    #urun_icerigi('parfum','parfum')
    urun_icerigi('cep_tel','cep_tel')
    #tum_kategori_linkleri()



