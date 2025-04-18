import curses
from curses import wrapper
from singleplayer import invert_boolean
from grid import Grid
import struct
import time

def invert_boolean(p):
    return not p


def interface(stdscr, factory=None):
    stdscr.clear()
    curses.curs_set(2) # set cursor visibility
    stdscr.nodelay(True) # don't stall the screen while waiting for the input
    keypress = None
    cursor_y,cursor_x = stdscr.getyx()

    while True:
        grid = factory.grid
        stdscr.clear()
        # display the curent state of the grid
        x,y = 0,0   
        while y < grid.height:
            while x < grid.width:
                #stdscr.addstr(y,x,str(grid.grid_list[(x,y)]))
                try:
                    stdscr.addstr(y,x,str(grid.grid_list[(x,y)]))
                except curses.error:
                    pass
                x += 1
            if x >= grid.width:
                x = 0
                y += 1

        # cursor movement
        stdscr.move(cursor_y, cursor_x)
        
        keypress = stdscr.getch()
        if keypress == curses.KEY_UP and cursor_y-1 >= 0:
            cursor_y -= 1
        elif keypress == curses.KEY_DOWN and cursor_y < grid.height-1:
            cursor_y += 1
        elif keypress == curses.KEY_RIGHT and cursor_x < grid.width-1:
            cursor_x += 1
        elif keypress == curses.KEY_LEFT and cursor_x-1 >= 0: 
            cursor_x -= 1

        # changing dead/alive state when spacebar hit 
        elif keypress == 32:
            pass
            #grid.edit(cursor_x,cursor_y)

        elif keypress == curses.KEY_END:
            return 

            
            

        
        
        stdscr.refresh()
        time.sleep(0.01666)

