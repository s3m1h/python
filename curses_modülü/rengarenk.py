import curses
import random
import time

BLOK = "  "
def main(stdscr):
    curses.curs_set(0)
    x,y = stdscr.getmaxyx() # x = 30 , y = 120 ==> x : düşey , y = yatay
    stdscr.nodelay(1)
    curses.start_color()
    stdscr.timeout(100)
    while True:
        blok = [
                random.randint(1,x-1),
                random.randint(1,y-1),
            ]
        print("blue: ",curses.COLOR_BLUE)   
        curses.init_pair(3,random.randint(1,10),random.randint(1,10))
        stdscr.addstr(blok[0],blok[1],BLOK,curses.color_pair(3))
        stdscr.refresh()
        time.sleep(0.05)
    
curses.wrapper(main)
input("Çıkmak için bir tuşa basın...")