import requests
from bs4 import BeautifulSoup


url ="https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"

r = requests.get(url)


soup = BeautifulSoup(r.content,"html.parser")

veri= soup.find_all("table",{"class": "chart full-width"})
#print(veri)

film_t = (veri[0].contents)[len(veri[0].contents)-2]
#print(film_t)
veri = film_t.find_all("tr")
#sonveri = veri.findall("td",{"class":"titleColumn"})

dosya = open("film_listesi.txt","w")
a = 0
for i in veri:
    basliklar = i.find_all("td",{"class":"titleColumn"})
    #print(basliklar)
    film_isim = basliklar[0].text
    film_isim = film_isim.replace("\n","")
    a+=1
    dosya.write("{}".format(a)+ "- "+film_isim+"\n")
dosya.close()

