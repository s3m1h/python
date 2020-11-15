from requests_html import AsyncHTMLSession, HTMLSession
import re
import time
#
from util import json_save
#
asession = AsyncHTMLSession()
####################################################3       
def hepsiburada_linkleri():
    session = HTMLSession()
    liste = []
    pattern = re.compile(r'p-[a-zA-Z]{3,}[0-9]{3,}[a-zA-Z0-9]{2,}') # regex şablonumuz # p-HBV00000Y8E0O 
    for a in range(1,50):
        url = "https://www.hepsiburada.com/ara?q=diz%C3%BCst%C3%BC+bilgisayar+laptop&sayfa={}".format(a)
        req = session.get(url)
        time.sleep(1)
        container = req.html.find('.product-list')[0]
        for i in container.absolute_links: # tüm linkler , all links
            r = re.search(pattern,i) 
            urun_kimligi = r.group() # çıktı, output, example: p-HBV00000Y8E0O
            print(urun_kimligi)
            liste.append(urun_kimligi)
    #json_save(liste, "hepsiburada_links")
####################################################3
async def laptop_urun_bilgileri():
    with open('hb_links.json','r') as f:
        linkler = json.load(f)
        for i in linkler:
            r = await asession.get("https://www.hepsiburada.com/laptop-notebook-dizustu-bilgisayarlar-"+i)
            time.sleep(2)
            name = r.html.find('.product-name')[0].text
            fiyat= r.html.find('.extra-discount-price')[0].text
            print("HB: ",name, fiyat)

if __name__ == '__main__':
    print(asession.run(laptop_urun_bilgileri))