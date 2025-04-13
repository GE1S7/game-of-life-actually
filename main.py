from grid import Grid
import curses
from curses import wrapper
import time
import random


def main(stdscr):
    siatka = Grid(80,40)
    siatka.init_grid()
    siatka.randomize()

    curses.curs_set(2) # set cursor visibility
    stdscr.nodelay(True) # don't stall the screen waiting for the input
    keypress = None
    cursor_y,cursor_x = stdscr.getyx()

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
        #time.sleep(0.00000000000001) # can use curses.napms(<ms>) instead

        # cursor movement
        stdscr.move(cursor_y, cursor_x)
        
        keypress = stdscr.getch()
        if keypress == curses.KEY_UP and cursor_y-1 >= 0:
            cursor_y -=1
        elif keypress == curses.KEY_DOWN and cursor_y < siatka.height-1:
            cursor_y += 1
        elif keypress == curses.KEY_RIGHT and cursor_x < siatka.width-1:
            cursor_x += 1
        elif keypress == curses.KEY_LEFT and cursor_x-1 >= 0: 
            cursor_x -= 1

        # changing dead/alive state when spacebar hit 
        if keypress == 32:
            siatka.edit(cursor_x,cursor_y)

        

        stdscr.refresh()



#main(curses.initscr())
wrapper(main)
