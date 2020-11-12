import requests
from bs4 import BeautifulSoup as bs
import urllib

def linkler():

    url = "https://wallhaven.cc/random"
    r = requests.get(url)
    soup = bs(r.content,"html.parser")
    li = soup.find(class_= "thumb-listing-page").ul.find_all("a",{"class":"preview"})
    liste = []
    for i in li:
        liste.append(i.get("href"))
        
    return liste
    
   
a = 0
while a != -1:
    for i in linkler():
        r2 = requests.get(i)
        soup2 = bs(r2.content,"html.parser")
        div = soup2.find(class_="scrollbox").find_all("img",{"id":"wallpaper"})

        for i in div:
            a += 1
            duvar_k = i.get("src")
            #print(duvar_k)
            r3 = requests.get(duvar_k)
            if r3.status_code == 200:
                with open("resim"+ str(a) +".jpg","wb") as f:
                    f.write(r3.content)
                    print(":)")
            else:
                print(":(")



