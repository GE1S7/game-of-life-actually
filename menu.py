import curses
class Menu():
    def __init__(self, width, height, pos_y_top, pos_x_top, options):
        self.width = width
        self.height = height
        self.posx = posx
        self.posy = posy
        self.posx_bot = posx

        self.menu_pad = curses.newpad(width, height)
        self.menu_panel = curses.panel.new_panel(menu_pad)

        self.super_menu = super_menu
        self.options = {"Singleplayer":, "Multiplayer":{"Co-op":, "Versus":""}}
        self.highlight_option = 0
        
        # has to be changing in the gameloop
        self.keypress = None

    def draw(self):
        self.menu_pad.border()
        self.menu_pad.addstr(0, 5, "MENU")
        for idx, x in enumerate(self.options.keys()):
            if self.highlight_option == idx:
                self.menu_pad.addstr(idx + 1, 1, f" {x} ", curses.A_REVERSE)
            else:
                self.menu_pad.addstr(idx + 1, 1, f" {x} ")



    def cursor_up(self):
        if highlight_opotion > 0:
            highlight_option -= 1

    def cursor_down(self):
        if highlight_option < len(current_option.keys() - 1):
            highlight_option += 1


    def choose_option:
        self.super_menu = self.options
        self.

    def go_topmenu(self):
        self.options = {"Singleplayer":, "Multiplayer":{"Co-op":, "Versus":""}}

    def menu_keys(self):
        if keypress == curses_END:
            return
        elif keypress == curses.KEY_UP:
            return
        
        




