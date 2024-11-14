#import pygame
import random
import time

class Grid():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid_list = {}

    def init_grid(self):
        grid_dict = {}
        for x in range(0,self.width):
            for y in range(0,self.height):
                self.grid_list[(x,y)] = 0

    def randomize(self):
        '''sets random dead/alive values for each cell in the grid'''
        for i in self.grid_list.keys():
            self.grid_list[i] = random.randint(0,1)

    def c_eval(self):
        '''evaluate the new value of cells in self.grid'''
        for x in  range(0, self.width):

            for y in range(0, self.height):

                neighbours = 0
                if x != 0 and x != self.width - 1 and y != 0 and y != self.height - 1:
                    for i in range(x-1,x+2):
                        for j in range(y-1,y+2):
                            if (i,j) == (x,y):
                                continue
                            if self.grid_list[(i, j)] == 1:
                                neighbours += 1
                #print(f"self.grid_list[({x},{y})] has {neighbours} neighbours")

                if neighbours in range(2,3):
                    self.grid_list[(x,y)] = 1

                else:
                    self.grid_list[(x,y)] = 0

    def game_over(self):
        for i in self.grid_list.values():
            if i != 0: 
                return False
        return True

siatka = Grid(10,10)
siatka.init_grid()
siatka.randomize()

generation = 1

while True:
    if siatka.game_over():
        break
    print(siatka.grid_list)
    siatka.c_eval()
    print("\n\n\n\n")
    generation += 1
    print(f"generation {generation} will start in 1 second")
    time.sleep(0.1)
