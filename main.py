from grid import Grid
import curses
from curses import wrapper
import time
import random
from singleplayer import singleplayer
from multiplayer import multiplayer

def invert_boolean(p):
    return not p

def main(stdscr, mode):
    if mode == "sp":
        singleplayer(stdscr)

    if mode == "mp":
        multiplayer(stdscr)





#main(curses.initscr())
wrapper(main, "mp")
