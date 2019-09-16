#!/usr/bin/python3

import unittest
from natemath import *


class MathTest(unittest.TestCase):

    # Test addValue function
    def testAddValue(self):
        self.assertEqual(addValue(10,5), 15)

    # Test subValue function
    def testsSubValue(self):
        self.assertEqual(subValue(10,5), 5)

    # Test multiValue function
    def testMultiValue(self):
        self.assertEqual(multiValue(10,5), 50)

    # Test divValue function
    def testDivValue(self):
        self.assertEqual(divValue(10,5), 2)

    # Test sqrtalue function
    def testSqrtValue(self):
        self.assertEqual(sqrtValue(9), 3)

    # Test expValue function
    def testExpValue(self):
        self.assertEqual(expValue(3,2), 9)

    # Test oct2Int function
    def testOct2Int(self):
        self.assertEqual(oct2Int(0o12), 10)

    # Test hex2Int function
    def testHex2Int(self):
        self.assertEqual(hex2Int(0xa), 10)

    # Test bin2Int function
    def testBin2Int(self):
        self.assertEqual(bin2Int(0b1010), 10)

    # Test hex2Oct function
    def testHex2Oct(self):
        self.assertEqual(hex2Oct(0xa), '0o12')

    # Test int2Oct function
    def testInt2Oct(self):
        self.assertEqual(int2Oct(10), '0o12')

    # Test bin2Oct function
    def testBin2Oct(self):
        self.assertEqual(bin2Oct(0b1010), '0o12')

    # Test oct2Hex function
    def testOct2Hex(self):
        self.assertEqual(oct2Hex(0o12), '0xa')

    # Test int2Hex function
    def testInt2Hex(self):
        self.assertEqual(int2Hex(10), '0xa')

    # Test bin2Hex function
    def testBin2Hex(self):
        self.assertEqual(bin2Hex(0b1010), '0xa')

    # Test oct2Bin function
    def testOct2Bin(self):
        self.assertEqual(oct2Bin(0o12), '0b1010')

    # Test int2Bin function
    def testInt2Bin(self):
        self.assertEqual(int2Bin(10), '0b1010')

    # Test hex2Bin function
    def testHex2Bin(self):
        self.assertEqual(hex2Bin(0xa), '0b1010')

if __name__ == '__main__':
    unittest.main()

