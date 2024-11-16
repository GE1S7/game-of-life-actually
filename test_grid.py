import unittest
from grid import Grid

class TestGrid(unittest.TestCase):
    def test_read(self):
        pass

    def test_square(self):
        '''square = still nature'''
        test_square = '''
░░░
░██
░██
'''
    


    def test_spinner(self):
        '''three squares in line spin'''
        test_line_horizontal = '''
░█░
░█░
░█░'''
        test_line_vertical = '''
░░░
███
░░░'''

        # test: vertical -> horizontal

        # test: horizontal -> vertical

    def test_three_two_one(self):
        '''boomerang folds and dies'''
        test_boomerang = '''
░█░
░░█
░█░''' 
        test_fold =░ '''
░░░
░██
░░░'''

        test_death = '''
░░░
░░░
░░░'''
