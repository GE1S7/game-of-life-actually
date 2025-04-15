from grid import Grid
import curses
from curses import wrapper
import time
import random
from singleplayer import singleplayer

def invert_boolean(p):
    return not p

def main(stdscr, mode):
    if mode == "sp":
        singleplayer(stdscr)




#main(curses.initscr())
wrapper(main, "sp")
