import random
import time

DEAD = "░"
ALIVE = "█"

class Grid():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid_list = {}

    def init_grid(self):
        grid_dict = {}
        for x in range(0,self.width):
            for y in range(0,self.height):
                self.grid_list[(x,y)] = DEAD

    def randomize(self):
        '''sets random dead/alive values for each cell in the grid'''
        for i in self.grid_list.keys():
            if random.randint(0,1) == 1:
                self.grid_list[i] = ALIVE
            else:
                self.grid_list[i] = DEAD

    def read(self, grin):
        grnsplt = grin.linesplit()
        self.height = len(grnsplt)
        self.width = len(grnsplt[0])

        for line in grnsplt:
            if len(line) != self.width:
                raise ValueError("width is not constant")
            x = 0
            for ch in line:
                

        
            


        


    def c_eval(self):
        '''evaluate the new value of cells in self.grid'''
        for x in  range(0, self.width):

            for y in range(0, self.height):

                neighbours = 0

                #if x != 0 and x != self.width - 1 and y != 0 and y != self.height - 1:

                for i in range(x-1,x+2):

                    #edges

                    for j in range(y-1,y+2):
                        if (i,j) == (x,y):
                            continue

                        if i == x-1 and x-1 < 0:
                            continue

                        if i > self.width - 1:
                            continue
                             #print(i)

                        if j == y-1 and  y-1 < 0:
                            continue
                             #print(j)

                        if j > self.height - 1:
                            continue
                            #print(j)

                        if self.grid_list[(i, j)] == ALIVE:
                            neighbours += 1

                #print(f"self.grid_list[({x},{y})] has {neighbours} neighbours")

                if neighbours in [2,3] and self.grid_list[(x,y)] == ALIVE: 
                    self.grid_list[(x,y)] = ALIVE

                elif neighbours == 3 and self.grid_list[(x,y)] == DEAD:
                    self.grid_list[(x,y)] = ALIVE

                else:
                    self.grid_list[(x,y)] = DEAD

    def game_over(self):
        for i in self.grid_list.values():
            if i != 0: 
                return False
        return True
