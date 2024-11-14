import unittest
from grid import Grid

class TestGrid(unittest.TestCase):
    def test_c_eval(self):
        siatka = Grid(100,100)
        siatka.init_grid()
        for i in siatka.grid_list.values():
            i = 1
        siatka.c_eval()

        self.assertEqual(siatka.grid_list[50,50],1)
