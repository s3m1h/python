from .filescan import Scan
import sqlite3 as sqlite
class FileScanManager:
    def __init__(self, scan:Scan):
        self.dosyalar = scan.tum_dosyalar()

    def goruntule_tum_dosyalar(self):
        for dosya in self.dosyalar:
            print(dosya)

    def goruntule_uzanti(self,uzanti):
        for dosya in self.dosyalar:
            if dosya["dosya_uzantisi"] == "."+ uzanti:
                print(dosya)

    def veritabanına_kaydet(self,isim):
        vt = sqlite.connect(str(isim))
        im = vt.cursor()
        tablo_yap  = """CREATE TABLE IF NOT EXISTS dosya 
        (
         dosya_adi TEXT,
         dosya_uzantisi TEXT,
         yol TEXT,
         tam_yol TEXT,
         son_degistirme TEXT,
         olusturma TEXT,
         dosya_boyutu TEXT)"""
        im.execute(tablo_yap)
        for dosya in self.dosyalar:
            değer_gir = f"""INSERT INTO dosya 
            VALUES ('{dosya["dosya_adi"]}',
             '{dosya["dosya_uzantisi"]}',
              '{dosya["yol"]}',
              '{dosya["tam_yol"]}',
              '{dosya["son_degistirme"]}',
              '{dosya["olusturma"]}',
              '{dosya["dosya_boyutu"]}')"""
            im.execute(değer_gir)
            vt.commit()
        vt.close()