import unittest, sys
sys.path.append('../')
from src.Chapter2 import Chapter2

class Chapter1Test(unittest.TestCase):
    # test class of Chapter1.py

    def setUp(self):
        self.target = Chapter2('../file/hightemp.txt')

    def test_method_10(self):
        self.assertTrue(self.target.wc(), 24)

    def test_method_11(self):
        self.target.sed()

if __name__ == '__main__':
    unittest.main()