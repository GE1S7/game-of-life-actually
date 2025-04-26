import unittest
from grid import Grid


class TestGrid(unittest.TestCase):
    def test_read_conversion(self):
        """square = still nature"""
        test_square = """
░░░
░██
░██"""
        test_grid_list = {
            (0, 0): "░",
            (1, 0): "░",
            (2, 0): "░",
            (0, 1): "░",
            (1, 1): "█",
            (2, 1): "█",
            (0, 2): "░",
            (1, 2): "█",
            (2, 2): "█",
        }

        g = Grid(1, 1)
        g.read(test_square)

        self.assertEqual(g.grid_list, test_grid_list)

    def test_square(self):
        """square = still nature"""
        test_square = """
░░░
░██
░██"""
        g = Grid(1, 1)
        g.read(test_square)
        tg = g.grid_list
        g.c_eval()

        self.assertEqual(g.grid_list, tg)

    def test_spinner(self):
        """three squares in line spin"""
        test_line_vertical = """
░█░
░█░
░█░"""
        test_line_horizontal = """
░░░
███
░░░"""
        vg = Grid(1, 1)
        hg = Grid(1, 1)

        vg.read(test_line_vertical)
        hg.read(test_line_horizontal)

        vg.c_eval()

        self.assertEqual(vg.grid_list, hg.grid_list)

        # test: vertical -> horizontal

        # test: horizontal -> vertical

    def test_three_two_one(self):
        """boomerang folds and dies"""
        test_boomerang = """
░█░
░░█
░█░"""
        test_fold = """
░░░
░██
░░░"""

        test_death = """
░░░
░░░
░░░"""
