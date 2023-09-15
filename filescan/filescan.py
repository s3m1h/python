import os
import time
import fnmatch

class Scan:
    dosyalar = dict()
    def __init__(self, path="C:/Users/semih", pattern = "*"):
        self.path = path
        self.pattern = pattern
    def tum_dosyalar(self):
        for root, dirs, files in os.walk(self.path):
            for value in files:
                if fnmatch.fnmatch(value,self.pattern):
                    dosya_adi = os.path.splitext(value)[0]
                    dosya_uzantisi = os.path.splitext(value)[1]
                    newpath = os.path.join(root, value).replace("\\", "/")
                    if os.path.isfile(newpath):
                        son_degistirme = time.ctime(os.path.getmtime(newpath))
                        olusturma = time.ctime(os.path.getctime(newpath))
                        dosya_boyutu = os.stat(newpath).st_size / 1024
                        yield {
                            "dosya_adi": dosya_adi,
                            "dosya_uzantisi":dosya_uzantisi,
                            "yol": root.replace("\\", "/"),
                            "tam_yol": newpath,
                            "son_degistirme":son_degistirme,
                            "olusturma":olusturma,
                            "dosya_boyutu": dosya_boyutu
                        }

