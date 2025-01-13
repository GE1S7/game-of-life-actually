from grid import Grid
import curses
from curses import wrapper
import time
import random

def main(stdscr):
    siatka = Grid(299,60)
    siatka.init_grid()
    siatka.randomize()

    #win = curses.newwin(siatka.height, siatka.width, 7, 20)

    generation = 1


    while True:       

        x,y = 0,0   
        while y < siatka.height:
            while x < siatka.width:
                try:
                    stdscr.addstr(y,x,str(siatka.grid_list[(x,y)]))
                except curses.error:
                    pass
                x += 1
            if x >= siatka.width:
                x = 0
                y += 1



        siatka.c_eval()
        generation += 1

        try:
            stdscr.addstr(siatka.height+1, 0, f"gen: {generation}")
            stdscr.addstr(siatka.height+2, 0, f"cursor_pos: {curses.getsyx()}")
        except curses.error:
            pass
        time.sleep(0.00000000001)
        
        stdscr.refresh()

wrapper(main)
