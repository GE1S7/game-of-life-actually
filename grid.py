import random
import time

# dead = "░"
# alive = "█"
dead = 0
alive = 1


class Grid():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid_list = {}
        self.selected = []

    def init_grid(self):
        grid_dict = {}
        for x in range(0,self.width):
            for y in range(0,self.height):
                self.grid_list[(x,y)] = dead

    def init_grid_tui(self):
        dead = "░"
        alive = "█"
        grid_dict = {}
        for x in range(0,self.width):
            for y in range(0,self.height):
                self.grid_list[(x,y)] = dead

    def randomize(self):
        '''sets random dead/alive values for each cell in the grid'''
        for i in self.grid_list.keys():
            if random.randint(0,1) == 1:
                self.grid_list[i] = alive
            else:
                self.grid_list[i] = dead

    def read(self, grin):
        grin = grin.lstrip()
        grin = grin.rstrip()
        self.init_grid()
        grnsplt = grin.split("\n")
        self.height = len(grnsplt)
        self.width = len(grnsplt[0])

        y = 0 
        for line in grnsplt:
            if line == "":
                continue
            if len(line) != self.width:
                raise ValueError("width is not constant")

            x = 0
            for ch in line:
                self.grid_list[(x,y)] = ch
                x += 1

            y += 1
        # print(self.grid_list)

    def select(self, x, y):
        if (x,y) not in self.selected:
            self.selected.append((x,y))

    def edit(self, x, y):
        if self.grid_list[(x,y)] == dead:
            self.grid_list[(x,y)] = alive
        elif self.grid_list[(x,y)] == alive:
            self.grid_list[(x,y)] = dead 



    def c_eval(self):
        new_grid_dict = {}
        '''evaluate the new value of cells in self.grid'''
        for x in  range(0, self.width):

            for y in range(0, self.height):
                # print(f"searching for neighbours of {(x,y)}")

                neighbours = 0

                #if x != 0 and x != self.width - 1 and y != 0 and y != self.height - 1:

                for i in range(x-1,x+2):
                    #edges
                    if i == x-1 and x-1 < 0:
                            continue

                    if i > self.width - 1:
                        continue
                         # print(i)


                    for j in range(y-1,y+2):
                        # print(f"checking for neighbour in: {(i,j)}")

                        if (i,j) == (x,y):
                            continue

                        if j == y-1 and  y-1 < 0:
                            continue
                             #print(j)

                        if j > self.height - 1:
                            continue
                            #print(j)

                        if self.grid_list[(i, j)] == alive:
                            neighbours += 1


                # print(f"self.grid_list[({x},{y})] has {neighbours} neighbours and is {self.grid_list[(x,y)]}")


                if neighbours == 3 and self.grid_list[(x,y)] == dead:
                    new_grid_dict[(x,y)] = alive

                elif neighbours < 4 and neighbours > 1 and self.grid_list[(x,y)] == alive: 
                    new_grid_dict[(x,y)] = alive

                else:
                    new_grid_dict[(x,y)] = dead

                # print(f"the field self.grid_list[({x},{y})] is now {new_grid_dict[(x,y)]}")
                
        self.grid_list = new_grid_dict
        # print(f"final dict {new_grid_dict}")


    def game_over(self):
        for i in self.grid_list.values():
            if i != 0: 
                return False
        return True
