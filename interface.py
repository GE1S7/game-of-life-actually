import curses
import curses.panel
from curses import wrapper
from singleplayer import invert_boolean
from grid import Grid
import struct
import time

def invert_boolean(p):
    return not p

def curses_display_setup(stdscr):
    curses.curs_set(1) # set cursor visibility
    curses.start_color()
    curses.use_default_colors()
    curses.can_change_color()
    #
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)
    stdscr.nodelay(True) # don't stall the screen while waiting for the input



def interface(stdscr, factory=None):
    DEAD = "░"
    ALIVE = "█"

    if factory is not None:
        grid = factory.grid

    cursor = stdscr.keypad(True)

    curses.curs_set(0) # set cursor visibility
    curses.start_color()
    curses.use_default_colors()
    curses.can_change_color()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)
    stdscr.nodelay(True) # don't stall the screen while waiting for the input

    keypress = None

    pad = curses.newpad(grid.height, grid.width)
    # pad position on stdscr
    padposx,padposy = (0,0)

    cursor_y,cursor_x = pad.getyx()
    # first visible line and column of the pad
    py,px = 0,0
    
    # size of terminal window
    window_size_y, window_size_x = stdscr.getmaxyx()

    # run menu on startup
    menu = True
    game = True 
    
    menu_width = 14
    menu_height = 16
    menu_pad = curses.newpad(14,16)
    menu_pos_y_top = window_size_y//2 - 7
    menu_pos_x_top = window_size_x//2 - 8
    menu_pos_y_bot = window_size_y//2 + 7
    menu_pos_x_bot = window_size_x//2 + 8

    menu_panel = curses.panel.new_panel(menu_pad)
    menu_panel.top()
    curses.panel.update_panels()

    menu_bars = ["sp", "mp"]


    while True:
        #stdscr.erase()
        menu_pad.erase()
        pad.erase()
        wpos_y_down = window_size_x
        keypress = stdscr.getch()

        if menu == True:
            menu_pad.border()
            menu_pad.addstr(0, 5, "MENU")
            menu_pad.addstr(1, 1, " Singleplayer ", curses.A_REVERSE) 
            menu_pad.addstr(2, 1, " Multiplayer ")
            for 
            
            if keypress == curses.KEY_END:
                return 
            if keypress == curses.KEY_DOWN:
                pass


        if game == True:

            # display the curent state of the grid
            x,y = 0,0   
            while y < grid.height:
                while x < grid.width:
                    try:
                        if (x,y) in grid.selected:
                            pad.addstr(y,x,str(grid.grid_list[(x,y)]), curses.color_pair(47))
                        else:
                            pad.addstr(y,x,str(grid.grid_list[(x,y)])),
                    except curses.error:
                        pass
                    x += 1
                if x >= grid.width:
                    x = 0
                    y += 1

            cy, cx = curses.getsyx()
            
            # size of pad (including the stuff outside the screen)
            #pad.addstr(py+cy+2,cx+10, f"pad_size: {str(pad.getmaxyx())}")

            # show id of key pressed
            #pad.addstr(py+cy+3, cx+1, f"key pressed: {keypress}")
            #pad.addstr(py+cy+4,cx+1, f"selected: {grid.selected}")
            #pad.border()
            #stdscr.border()






            # cursor movement
            pad.move(cursor_y, cursor_x)
            if (keypress == curses.KEY_UP or keypress == 107) and cursor_y-1 >= 0:
                cursor_y -= 1
                if 5 >=  cy and py > 0:
                    py -= 1
            elif (keypress == curses.KEY_DOWN or keypress == 106) and cursor_y < grid.height-1:
                cursor_y += 1
                if window_size_y - 5 <=  cy: 
                    py += 1
            elif (keypress == curses.KEY_RIGHT or keypress == 108) and cursor_x < grid.width-1:
                cursor_x += 1
                if window_size_x - 5 <=  cx and px > 0:
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
                    if factory is not None:
                        for i in range(0,len(grid.selected)):
                            factory.client[0].sendCoord(*grid.selected[i])
                    else:
                        for cell in grid.selected:
                            grid.edit(cell[0], cell[1])
                        
                    grid.selected = []


                    #for cell in grid.selected:
                    #    factory.client[0].sendCoord(cell[0], cell[1])
                        
                else:
                    if factory is not None:
                        factory.client[0].sendCoord(cursor_x,cursor_y)
                    else:
                        grid.edit(cursor_x,cursor_y)

            elif keypress == curses.KEY_END:
                return 

            #print(f"\n\nnwindow size: {stdscr.getmaxyx()}")
            #print(f"py, px: {py},{px}; cy, cx: {cy},{cx}; WinSize: {window_size_y},{window_size_x}; key: {keypress}")
            #print("py: ", py, "window size y: ", window_size_y, "cursor_y ", cursor_y)
        
        if game == True:
            #stdscr.refresh()
            stdscr.noutrefresh()
            pad.noutrefresh(py, px, padposy+1, padposx+1, window_size_y-1, window_size_x-1) 
        if menu == True:
            menu_pad.noutrefresh(0,0, menu_pos_y_top, menu_pos_x_top, menu_pos_y_bot, menu_pos_x_bot)
        curses.doupdate()
        time.sleep(0.01666)
