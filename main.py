from grid import Grid
import curses
from curses import wrapper
import time

stdscr = curses.initscr()

curses.noecho()
curses.cbreak()
stdscr.keypad(True)

siatka = Grid(9,9)
siatka.init_grid()
siatka.randomize()

#win = curses.newwin(siatka.height, siatka.width, 7, 20)

generation = 1

while True:
    #if siatka.game_over():
        #break
        
    x,y = 0,0   
    while y < siatka.height:
        while x < siatka.width:
            stdscr.addstr(y,x,str(siatka.grid_list[(x,y)]))
            x += 1
        if x >= siatka.width:
            x = 0
            y += 1

    siatka.c_eval()
    generation += 1
    stdscr.addstr(siatka.height+1, 0, f"gen: {generation}")
    time.sleep(0.5)
    stdscr.refresh()

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
