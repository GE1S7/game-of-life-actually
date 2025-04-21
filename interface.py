import curses
from curses import wrapper
from singleplayer import invert_boolean
from grid import Grid
import struct
import time

def invert_boolean(p):
    return not p


def interface(stdscr, factory=None):
    DEAD = "░"
    ALIVE = "█"

    grid = factory.grid
    stdscr.clear()

    curses.curs_set(1) # set cursor visibility
    curses.start_color()
    curses.use_default_colors()
    curses.can_change_color()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)
    stdscr.nodelay(True) # don't stall the screen while waiting for the input
    keypress = None
    
    pad = curses.newpad(grid.height, grid.width)
    padposx,padposy = (0,0)
    cursor_y,cursor_x = pad.getyx()
    py,px = 0,0



    while True:
        stdscr.erase()
        pad.erase()
        window_size_y, window_size_x = stdscr.getmaxyx()
        wpos_y_down = window_size_x
        # display the curent state of the grid
        x,y = 0,0   
        while y < grid.height:
            while x < grid.width:
                try:
                    if (x,y) in grid.selected:
                        pad.addstr(y,x,str(grid.grid_list[(x,y)]), curses.color_pair(47))
                    else:
                        pad.addstr(y,x,str(grid.grid_list[(x,y)]))
                except curses.error:
                    pass
                x += 1
            if x >= grid.width:
                x = 0
                y += 1

        for cell in grid.selected:
            pad.addch(cell[1], cell[0], str(grid.grid_list[cursor_x,cursor_y]), curses.A_DIM)
            pad.addch(cell[1], cell[0], str(grid.grid_list[cursor_x,cursor_y]), curses.color_pair(47))
        cy, cx = curses.getsyx()
        # For testing purposes:
        # display cursor location
        #pad.addstr(py+cy, cx+1, f"cy, cx: {str(curses.getsyx())}")
        #pad.addstr(py+cy+1,cx+1, f"py, px: {str((py,px))}")
        
        # size of the visible window
        #pad.addstr(py+cy+2, x+1, f"stdscr_size: {str(stdscr.getmaxyx())}")

        # size of pad (including the stuff outside the screen)
        #pad.addstr(py+cy+2,cx+10, f"pad_size: {str(pad.getmaxyx())}")

        # show id of key pressed
        #pad.addstr(py+cy+3, cx+1, f"key pressed: {keypress}")
        #pad.addstr(py+cy+4,cx+1, f"selected: {grid.selected}")
        #pad.border()






        # cursor movement
        pad.move(cursor_y, cursor_x)
        keypress = stdscr.getch()
        if (keypress == curses.KEY_UP or keypress == 107) and cursor_y-1 >= 0:
            cursor_y -= 1
            if 5 >=  cy:
                py -= 1
        elif (keypress == curses.KEY_DOWN or keypress == 106) and cursor_y < grid.height-1:
            cursor_y += 1
            if window_size_y - 5 <=  cy:
                py += 1
        elif (keypress == curses.KEY_RIGHT or keypress == 108) and cursor_x < grid.width-1:
            cursor_x += 1
            if window_size_x - 5 <=  cx:
                px += 1
        elif (keypress == curses.KEY_LEFT or keypress == 104) and cursor_x-1 >= 0: 
            cursor_x -= 1
            if 5 >=  cx:
                px -= 1
        # select cell
        elif keypress == 118:
            grid.select(cursor_x, cursor_y)


        # changing dead/alive state when spacebar hit 
        elif keypress == 32:
            if grid.selected != []:
                for i in range(0,len(grid.selected)):
                    factory.client[0].sendCoord(*grid.selected[i])
                    
                grid.selected = []


                #for cell in grid.selected:
                #    factory.client[0].sendCoord(cell[0], cell[1])
                    
            else:
                factory.client[0].sendCoord(cursor_x,cursor_y)
            # sp
            #grid.edit(cursor_x,cursor_y)

        elif keypress == curses.KEY_END:
            return 

        #print(f"\n\nnwindow size: {stdscr.getmaxyx()}")
        #print("py, px: ", py, px)
        #print("py: ", py, "window size y: ", window_size_y, "cursor_y ", cursor_y)
        
        stdscr.refresh()
        pad.refresh(py, px, padposy, padposx, window_size_y-1, window_size_x-1) 
        time.sleep(0.01666)
