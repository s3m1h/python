import curses
import time
import random
from curses import textpad

BLOK = '▀'
SOL = curses.KEY_LEFT
SAG = curses.KEY_RIGHT
ASAGI = curses.KEY_DOWN
YUKARI = curses.KEY_UP
SPEED = 100

def create_food(snake,box):
    food = None
    while food is None:
        food = [
        random.randint(box[0][0]+1,box[1][0]-1),
        random.randint(box[0][1]+1,box[1][1]-1),
        ]
        if food in snake:
            food = None
    return food

    
  
def main(ekran):

    boyut0, boyut1 = ekran.getmaxyx()
    curses.curs_set(0)
    ekran.nodelay(1)
    ekran.timeout(SPEED)
    #ekran = curses.initscr()
    
    box = [[1,1], [boyut0 //2+5,boyut1-3]]
    textpad.rectangle(ekran,box[0][0],box[0][1],box[1][0],box[1][1])
    
    
    snake = [[boyut0//2,boyut1//2+1],
            [boyut0//2,boyut1//2],
            [boyut0//2,boyut1//2-1]]
    #print(boyut0,boyut1)
    direction = SAG
    for y,x in snake:
        ekran.addstr(y,x,BLOK)
        
    # Elma ilk
    food = create_food(snake,box)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_YELLOW) 
    ekran.addstr(food[0],food[1],BLOK,curses.color_pair(3))
    ekran.refresh()
    # --------
    
    
    puan = 0
    curses.start_color()
    
    while True:
        key = ekran.getch()
        
        if key in [SAG,SOL,ASAGI,YUKARI]:
            direction = key
        head = snake[0]
       
        if direction == SAG:
            new_head = [head[0],head[1]+1]
        elif direction == SOL:
            new_head = [head[0],head[1]-1]
        elif direction == YUKARI:
            new_head = [head[0]-1,head[1]]
        elif direction == ASAGI:
            new_head = [head[0]+1,head[1]]
        
        # new_head i sıfırıncı indexr at yani başa geç
        
        snake.insert(0,new_head)
        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLUE) 
        ekran.addstr(new_head[0],new_head[1],BLOK,curses.color_pair(1))
        ekran.refresh()
        
        ######  Bilgiler #####
        ekran.addstr(boyut0//2+10,boyut1//2-50,"PUAN: {}".format(puan))
        ekran.addstr(boyut0//2+11,boyut1//2-50,"SNAKE HEAD: {}".format(snake[0]))
        #ekran.addstr(boyut0//2+12,boyut1//2-50,"SNAKE KORD.: {}".format(snake))
       
        ######################
        if snake[0] == food:
            food = create_food(snake,box)
            # Elma
            ekran.refresh()
            curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_GREEN) 
            ekran.addstr(food[0],food[1],BLOK,curses.color_pair(2))
            
            puan += 10
        else:
            ekran.addstr(snake[-1][0],snake[-1][1],' ')
            snake.pop()
        
        
        # DUVARLARA ÇARPMA
        if(snake[0][0] in [box[0][0],box[1][0]] or
            snake[0][1] in [box[0][1],box[1][1]] or
            snake[0] in snake[1:]):
            msg = "GAME OVER! SKOR: {}".format(puan)
            ekran.addstr(boyut0//2,boyut1//2 -len(msg)//2,msg)
            ekran.nodelay(0)
            ekran.getch()
            time.sleep(1)
            break
        
        ekran.refresh()
    
curses.wrapper(main)
input("Çıkmak için enter e bas")
