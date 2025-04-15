import curses
from curses import wrapper
from singleplayer import invert_boolean
from grid import Grid
import struct
from twisted.internet.protocol import Protocol

def multiplayer(stdscr):
    pause = True
    siatka = Grid(32,32)
    siatka.init_grid()
    
    curses.curs_set(2) # set cursor visibility
    stdscr.nodelay(True) # don't stall the screen while waiting for the input
    keypress = None
    cursor_y,cursor_x = stdscr.getyx()

    while True:
        # display the curent state of the grid
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

        if pause == False: 
            siatka.c_eval()
            
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


        # (un)pause
        if keypress == 112:
            pause = invert_boolean(pause)

        
        stdscr.refresh()
