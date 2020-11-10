import requests
from bs4 import BeautifulSoup as bs
import json
###
from util import json_save
URL = {

    'trdublaj': 'https://www.diziyo8.net/dizi-listesi-turkce-dublaj/',
    'traltyazi': 'https://www.diziyo8.net/dizi-listesi-turkce-altyazi/',
    'anime': 'https://www.diziyo8.net/dizi-listesi-anime/',
    'asya': 'https://www.diziyo8.net/dizi-listesi-asya/',
    'yerlidizi': 'https://www.diziyo8.net/dizi-listesi-yerli-dizi/',
}
def diziyo8():
    req = requests.get(URL['trdublaj'])
    soup = bs(req.content, 'html.parser')
    items = {}
    for i in soup.find('div',{'class':'dizi_turleri'})('a'):
        name = i.font.text.lower().replace('ü','u').replace('ğ','g').replace('ı','i').replace('ç','c').replace('â€¢','').replace('!','').replace('(anime)','')
        link = i.get('href')
        items[name.strip().replace(':','.').replace('.','').replace('(tã¼rkã§e dublaj)','')] = link
    json_save(items,'trdublaj')
    return items
def film_scrapy():
    items = {}
    with open('trdublaj.json','r') as f:
        data = json.load(f)
        for i in data.keys():
            url = data[i]
            req = requests.get(url)
            soup = bs(req.content, 'html.parser')
            ###
            poster = soup.find('div',{'class':'poster'})('img')[0]['src']
            name = soup.find('div',{'class':'data'})('h1')[0].text
            date = soup.find('span',{'class':'date'}).text
            rating = soup.find('span',{'class':'dt_rating_vgs'}).text
            rating_count = soup.find('span',{'class':'rating-count'}).text
            #imdb = soup.find('div',{'class':'data'}).find_all('div',{'class':'extra'})[1]('b')[0].text
            seasons = soup.find('div',{'id':'seasons'}).find_all('div',{'class':'se-q'})
            seasons_items = []
            for j in seasons:
                count = j('span')[0].text
                date = j('span')[1].text
                seasons_data = {
                    f'{count}.sezon':date,
                }
                seasons_items.append(seasons_data)
            new_data = {
                'poster':poster,
                'date':date,
                'rating':rating,
                'rating_count':rating_count,
                'seasons':seasons_items,
            }
            items[name] = new_data
    json_save(items,'filmler')
                
if __name__ =='__main__':
    #diziyo8()
    film_scrapy()