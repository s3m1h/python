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

    'populerdiziler': {
        'La casa de papel': 'https://www.diziyo8.net/dizi-izle/la-casa-de-papel-turkce-dublaj-hd-izle/',
        'Riverdale': 'https://www.diziyo8.net/dizi-izle/riverdale-turkce-dublaj-hd-izle/',
        'Stranger Things': 'https://www.diziyo8.net/dizi-izle/stranger-things-turkce-dublaj-hd-izle/',
        'The 100': 'https://www.diziyo8.net/dizi-izle/the-100-turkce-dublaj-hd-izle/',
        'Narcos': 'https://www.diziyo8.net/dizi-izle/narcos-turkce-dublaj-hd-izle/',
        'Sex Education': 'https://www.diziyo8.net/dizi-izle/sex-education-turkce-dublaj-hd-izle/',
        'Titans': 'https://www.diziyo8.net/dizi-izle/titans-turkce-dublaj-hd-izle/',
        'Peaky Blinders': 'https://www.diziyo8.net/dizi-izle/peaky-blinders-turkce-dublaj-hd-izle/',
        'Rick and Morty': 'https://www.diziyo8.net/dizi-izle/rick-and-morty-turkce-dublaj-hd-izle/',
        'Insatiable': 'https://www.diziyo8.net/dizi-izle/insatiable-turkce-dublaj-hd-izle/',
        'The Umbrella Academy': 'https://www.diziyo8.net/dizi-izle/the-umbrella-academy-turkce-dublaj-hd-izle/',
        'Baby': 'https://www.diziyo8.net/dizi-izle/baby-turkce-dublaj-hd-izle/',
        'Dexter': 'https://www.diziyo8.net/dizi-izle/dexter-turkce-dublaj-hd-izle/',
    }
}


def diziyo8():
    req = requests.get(URL['yerlidizi'])
    soup = bs(req.content, 'html.parser')
    items = {}
    for i in soup.find('div', {'class': 'dizi_turleri'})('a'):
        name = i.font.text.lower().replace('ü', 'u').replace('ğ', 'g').replace(
            'ı', 'i').replace('ç', 'c').replace('â€¢', '').replace('!', '').replace('(anime)', '')
        link = i.get('href')
        items[name.strip().replace(':', '.').replace(
            '.', '').replace('(tã¼rkã§e dublaj)', '')] = link
    json_save(items, 'yerlidizi')
    return items


def view_scrapy(data):
    items = {}
    for i in data.keys():
        url = data[i]
        req = requests.get(url)
        soup = bs(req.content, 'html.parser')
        ###
        poster = soup.find('div', {'class': 'poster'})('img')[0]['src']
        name = soup.find('div', {'class': 'data'})('h1')[0].text
        date = soup.find('span', {'class': 'date'}).text
        rating = soup.find('span', {'class': 'dt_rating_vgs'}).text
        rating_count = soup.find('span', {'class': 'rating-count'}).text
        #imdb = soup.find('div',{'class':'data'}).find_all('div',{'class':'extra'})[1]('b')[0].text
        seasons = soup.find('div', {'id': 'seasons'}).find_all(
            'div', {'class': 'se-q'})
        seasons_items = []
        for j in seasons:
            count = j('span')[0].text
            date = j('span')[1].text
            seasons_data = {
                f'{count}.sezon': date,
            }
            seasons_items.append(seasons_data)
        new_data = {
            'poster': poster,
            'date': date,
            'rating': rating,
            'rating_count': rating_count,
            'seasons': seasons_items,
        }
        items[name] = new_data
    return items


def film_scrapy():
    # filmlistesi/yerlidizi.json
    # filmlistesi/trdublaj.json
    # filmlistesi/anime.json
    # filmlistesi/asya.json
    # filmlistesi/yerlidizi.json
    with open('filmlistesi/yerlidizi.json', 'r') as f:
        data = json.load(f)
        json_save(view_scrapy(data),'yerlidizi_')
    
def popular(name):
    url = URL['populerdiziler'][name]
    req = requests.get(url)
    soup = bs(req.content, 'html.parser')
    print(soup)


if __name__ == '__main__':
    #popular('La casa de papel')
    #diziyo8()
    film_scrapy()
