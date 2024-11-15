from grid import Grid
import curses

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

siatka = Grid(10,10)
siatka.init_grid()
siatka.randomize()

generation = 1

while True:
    if siatka.game_over():
        break
    print(siatka.grid_list, end="\r")
    siatka.c_eval()
    #print("\n\n\n\n")
    generation += 1
    #print(f"generation {generation} will start in 1 second")
    time.sleep(0.1)


curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
