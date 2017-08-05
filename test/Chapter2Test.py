import unittest
import sys

sys.path.append('../')
from src.Chapter2 import Chapter2


class Chapter2Test(unittest.TestCase):
    def setUp(self):
        self.target = Chapter2('../file/hightemp.txt')

    def test_method_10(self):
        self.assertTrue(self.target.method_10(), 24)

    def test_method_11(self):
        self.target.method_11()

    def test_method_12(self):
        self.target.method_12()

    # paste -d"\t" col1.txt col2.txt
    def test_method_13(self):
        self.target.method_13()

    # head -5 hightemp.txt
    def test_method_14(self):
        self.target.method_14(5)

    def test_method_15(self):
        print('\n')
        self.target.method_15(35)

    def test_method_16(self):
        self.target.method_16(3)

    # cut -f 1 hightemp.txt | sort | uniq
    def test_method_17(self):
        self.target.method_17()

    def test_method_18(self):
        self.target.method_18()

    def test_method_19(self):
        self.target.method_19()

if __name__ == '__main__':
    unittest.main()
