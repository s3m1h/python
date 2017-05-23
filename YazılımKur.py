import os
def fonksiyon():
    print("""
    <---- Hosgeldin ---->
    |                   |
    |    (1) Giris      |
    |    (q) Çıkıs      |
    |                   |
    <------------------->
       """)
    giriş = input('> ')
    if giriş == '1':
        while True:
            print("""
                <------------ (p) Pacman'ı Güncelle ------------->
                |  (1) Plank             (11) Pycharm-community  |
                |  (2) Screenfetch       (12) İpython            |
                |  (3) Virtualbox        (13) Vim                |
                |  (4) Yaourt            (14) Atom editor        |        
                |  (5) Google-chrome     (15) Axel Downloader    |
                |  (6) Chromium          (16) Pepper-Flash       |
                |  (7) Midori            (17) MintStick          |
                |  (8) Opera             (18) Qbittorrent        |
                |  (9) Sublime editor    (19) Transmission       |
                |  (10) Gedit            (q) Çıkış               |
                <------------------------------------------------>
            """)
            giriş2 = input('> ')
            if giriş2 == 'p':
                print('Pacman güncellemesi başlatılıyor...\n')
                os.system('sudo pacman -Syyu')
            elif giriş2 == '1':
                print("Plank kurulumu başlatılıyor...\n")
                os.system('sudo pacman -S plank')
            elif giriş2 == '2':
                print("Screenfetch kurulumu başlatılıyor...\n")
                os.system('sudo pacman -S screenfetch')
            elif giriş2 == '3':
                print('VirtualBox kurulumu başlatılıyor...\n')
                os.system('sudo pacman -S virtualbox')
            elif giriş2 == '4':
                print('Yaourt kurulumu başlatılıyor...\n')
                os.system('sudo pacman -S yaourt')
            elif giriş2 == '5':
                print('Google-chrome kurulumu başlatılıyor...\n')
                os.system('yaourt -S google-chrome')
            elif giriş2 == '6':
                print('Chromium kurulumu başlatılıyor...\n')
                os.system('sudo pacman -S chromium')
            elif giriş2 == '7':
                print('Midori kurulumu başlatılıyor...\n')
                os.system('sudo pacman -S midori')
            elif giriş2 == '8':
                print('Opera kurulumu başlatılıyor...\n')
                os.system('sudo pacman -S opera')
            elif giriş2 == '9':
                print('Sublime-text editor kurulumu başlatılıyor...\n')
                os.system('yaourt -S sublime-text ')
            elif giriş2 == '10':
                print('Gedit editor kurulumu başlatılıyor...\n')
                os.system('sudo pacman -S gedit')
            elif giriş2 == '11':
                print('Pycharm-Community kurulumu başlatılıyor...\n')
                os.system('yaourt -S pycharm-community')
            elif giriş2 == '12':
                print('İpython kurulumu başlatılıyor...\n')
                os.system('sudo pacman -S ipython')
            elif giriş2 == '13':
                print('Vim kurulumu başlatılıyor...\n')
                os.system('sudo pacman -S vim')
            elif giriş2 == '14':
                print('Atom kurulumu başlatılıyor...\n')
                os.system('sudo pacman -S atom')
            elif giriş2 == '15':
                print('Axel kurulumu başlatılıyor...\n')
                os.system('sudo pacman -S axel')
            elif giriş2 == '16':
                print('Pepper-flash kurulumu başlatılıyor...\n')
                os.system('yaourt pepper-flash')
            elif giriş2 == '17':
                print('Mintstick kurulumu başlatılıyor...\n')
                os.system('yaourt mintstick-git')
            elif giriş2 == '18':
                print('Qbittorrent kurulumu başlatılıyor...\n')
                os.system('sudo pacman -S qbittorrent')
            elif giriş2 == '19':
                print('Transmission kurulumu başlatılıyor...\n')
                os.system('sudo pacman -S transmission-gtk')
            elif giriş2 == 'q':
                print('Çıkış yapıldı...')
                break
            else:
                print('Hatalı giriş yaptınız.Tekrar deneyin! ')
    elif giriş == 'q':
        print("Çıkış yapıldı...")
    else:
        print('Hata! çıkılıyor...')

if __name__ == '__main__':
    fonksiyon()