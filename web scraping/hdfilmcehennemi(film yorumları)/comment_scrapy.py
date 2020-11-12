def hdfilmcehennemi():
    for page in range(51):
        url = 'https://www.hdfilmcehennemi.net/tur/bilim-kurgu-filmleri-izleyin/page/{}/'.format(page+1)
        req = requests.get(url)
        soup = bs(req.content,'html.parser')
        filmler = soup.find('div',{'class':'tab-content'}).find_all('div',{'class':'poster-container'})
        for film in filmler:
            link = film.a.get('href')
            name = film.div.get('data-original-title').replace('izle','').replace(':','').replace(' ','').lower()
            ####### COMMENTS
            #url = "https://www.hdfilmcehennemi.net/warrior-2-sezon-izle/comment-page-1/#comments"
            rq = requests.get(link+'comment-page-1/#comments')
            soup2 = bs(rq.content,'html.parser')
            comment_list = soup2.find('div',{'class':'yorum-listesi'})
            if comment_list.text == '':
                print("{} filmine yorum yapılmamıştır".format(name))
                continue
            else:
                comment_list = soup2.find('div',{'class':'yorum-listesi'})('ol')[0].find_all('li')
                print("--------------",name.upper(),"-----------------")
                for i in comment_list:
                    nick_name = i.find('div',{'class':'comment-author'}).cite.text
                    # ana yorum
                    main_comment = i('div')[0].find('p').text
                    print(f"|{nick_name}| ",main_comment.lower())
                    if i('ul') == []:
                        continue
                    else:
                        for j in i('ul'):
                            # alt yorum
                            print("---",j('p')[0].text)
                        print('------------------------------------------------')
                        
if __name__ == '__main__':
    hdfilmcehennemi()