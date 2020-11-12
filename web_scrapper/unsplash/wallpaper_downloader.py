import requests
import urllib
import os
#import time
from bs4 import BeautifulSoup as bs
#from tqdm import tqdm


class Wallpapers():
    def __init__(self):
        print("program çalıştırıldı")
        self.a = []
        self.k_adı = ''
        self.kullanıcı_adı()

    def kullanıcı_adı(self):
        #k_adı = ''
        suanki_dizin = os.getcwd().split("\\")
        for i in range(len(suanki_dizin)):
            if suanki_dizin[i] == 'Users':
                self.k_adı = suanki_dizin[i + 1]
        return self.k_adı


    def dow(self,DK_ismi):

        if DK_ismi == 'android' or DK_ismi == 'desktop' or DK_ismi == 'animals':
            link_ = "https://unsplash.com/wallpapers/{}".format(DK_ismi)
        else:
            link_ = "https://unsplash.com/wallpapers/nature/{}".format(DK_ismi)
        # --------------------------------------------------------------------------indirme_linkleri------------#
        r = requests.get(link_)
        if r.status_code == 200:
            soup = bs(r.content, "html.parser")
            div_e = soup.find_all("a", {"class": "_1hjZT _1jjdS _1CBrG _1WPby xLon9 Onk5k _17avz _1B083 _3d86A"})
            for i in div_e:
                self.a.append(i.get("href"))
        else:
            print("bağlantı başarısız oldu...")
        #-------------------------------------------------------------------------------------------------------#

        yeni_klasör = input("Masaüstünde duvar kağıtlarının indirileceği yeni bir klasör adı gir...\n> ")
        os.chdir("C:\\Users\\{}\\Desktop".format(self.kullanıcı_adı()))  # dosya yolunu değiştir
        os.mkdir("{}".format(yeni_klasör))  # yeni klasör adını formatla ve oluştur

        say = 1
        for i in self.a:
            os.chdir("C:\\Users\\{}\\Desktop\\{}".format(self.kullanıcı_adı(), yeni_klasör))  # dosya yolunu yeniden değiştir
            urllib.request.urlretrieve(i, "resim" + str(say) + ".jpg")
            print("o", end=" ")
            say += 1
        print("İndirme başarılı bir şekilde tamamlandı...")

    def f(self):
        print("""
        -------------------------------------------------------------------------
            |1|  | HD Doğa Duvar Kağıtları      |3| Masaüstü Duvar Kağıtları  |
            ------------------------------------------------------------------
            |2|  | HD Android Duvar Kağıtları   |4| Hayvanlar Duvar kağıtları |
        -------------------------------------------------------------------------
           """)
        giriş = input('> ')
        if giriş == '1':
            while True:
                print("""
                        ----------------------------------
                            | HD Doğa Duvar Kağıtları |
                        ----------------------------------
                            |1| stone       |4| rainbow
                            |2| water       |5| snow
                            |3| moon        |6| cloud
                """)
                giris2 = input('> ')

                if giris2 == '1':
                    print("stone(taş) duvar kağıtlarını seçtiniz...")
                    w.dow("stone")
                elif giris2 == '2':
                    print("water(su) duvar kağıtlarını seçtiniz...")
                    w.dow("water")
                elif giris2 == '3':
                    print("moon(ay) duvar kağıtlarını seçtiniz...")
                    w.dow("moon")
                elif giris2 == '4':
                    print("rainbow(gökkuşağı) duvar kağıtlarını seçtiniz...")
                    w.dow("rainbow")
                elif giris2 == '5':
                    print("snow(kar) duvar kağıtlarını seçtiniz...")
                    w.dow("snow")
                elif giris2 == '6':
                    print("cloud(bulut) duvar kağıtlarını seçtiniz...")
                    w.dow("cloud")
                else:
                    print("hatalı giriş...")

        elif giriş == '2':
            print("HD Android duvar kağıtlarını seçtiniz...")
            w.dow("android")
        elif giriş == '3':
            print("HD Masaüstü duvar kağıtlarını seçtiniz...")
            w.dow("desktop")
        elif giriş == '4':
            print("HD Hayvanlar duvar kağıtlarını seçtiniz...")
            w.dow("animals")
        else:
            print("HATAAAA")
w = Wallpapers()
w.f()


