#!/usr/bin/python3

# Title: Test Nate's Basic Math Module
# Author: Nathan Gregg
# Date: 2019.09.24


"""Basic Math Module unit test program written in Python3.  This program
tests all functions provided by the natemath module to ensure it returns
the proper values.

"""


import unittest
from natemath import *


class MathTest(unittest.TestCase):

    # Test addValue function
    def  testAddValue(self):

        """Testing adding two values 

        Parameters:
        value1 (int): 10
        value2 (int): 5

        Returns:
        float: 15

        """

        self.assertEqual(addValue(10,5), 15)

    # Test subValue function
    def testsSubValue(self):

        """Test substracting two values 

        Parameters:
        value1 (int): 10
        value2 (int): 5

        Returns:
        float: 5

        """

        self.assertEqual(subValue(10,5), 5)

    # Test multiValue function
    def testMultiValue(self):

        """Testing multiplying two values 

        Parameters:
        value1 (int): 10
        value2 (int): 5

        Returns:
        float: 50

        """

        self.assertEqual(multiValue(10,5), 50)

    # Test multiValue function with floating numbers
    def testMultiValueFloat(self):

        """Testing multiplying two floating values 

        Parameters:
        value1 (float): 3.333333
        value2 (float): 2.0

        Returns:
        float: 6.666

        """

        self.assertAlmostEqual(multiValue(3.333333,2.0), 6.66666, places=3)

    # Test divValue function
    def testDivValue(self):

        """Test dividing two values 

        Parameters:
        value1 (int): 10
        value2 (int): 5

        Returns:
        float: 2

        """

        self.assertEqual(divValue(10,5), 2)

    # Test divValue function with floating numbers
    def testDivValueFloat(self):

        """Test dividing two floating values 

        Parameters:
        value1 (int): 6.66666,
        value2 (int): 2.0

        Returns:
        float: 3.3333

        """

        self.assertAlmostEqual(divValue(6.66666,2.0), 3.33333, places=3)

    # Test sqrtalue function
    def testSqrtValue(self):

        """Testing finding square root of value

        Parameters:
        value (int): 9

        Returns:
        float: 3

        """

        self.assertEqual(sqrtValue(9), 3)

    # Test sqrtalue function with floating number
    def testSqrtValueFloat(self):

        """Testing finding square root of value with floating numbers

        Parameters:
        value (float): 10

        Returns:
        float: 3.16227

        """

        self.assertAlmostEqual(sqrtValue(10), 3.16227, places=3)

    # Test expValue function
    def testExpValue(self):

        """Testing finding expondent value

        Parameters:
        value1 (int): 3
        value2 (int): 2

        Returns:
        float: 9

        """

        self.assertEqual(expValue(3,2), 9)

    # Test expValue function with floating numbers
    def testExpValueFloat(self):

        """Testing finding expondent value with floating numbers

        Parameters:
        value1 (float): 3.16227
        value2 (float): 2.0

        Returns:
        float: 9.99995

        """

        self.assertAlmostEqual(expValue(3.16227,2.0), 9.99995, places=3)

    # Test oct2Int function
    def testOct2Int(self):

        """Testing converting octal number to integer.

        Parameters:
        value (octal): 0o12

        Returns:
        string: 10

        """

        self.assertEqual(oct2Int(0o12), 10)

    # Test hex2Int function
    def testHex2Int(self):

        """Testing converting hexadecimal number to integer.

        Parameters:
        value (hexadecimal): 0xa

        Returns:
        string: 10

        """

        self.assertEqual(hex2Int(0xa), 10)

    # Test bin2Int function
    def testBin2Int(self):

        """Testing converting binary number to integer.

        Parameters:
        value (binary): 0b1010

        Returns:
        string: 10

        """

        self.assertEqual(bin2Int(0b1010), 10)

    # Test hex2Oct function
    def testHex2Oct(self):

        """Testing converting hexadecimal number to octal.

        Parameters:
        value (octal): 0xa

        Returns:
        string: 0o12

        """

        self.assertEqual(hex2Oct(0xa), '0o12')

    # Test int2Oct function
    def testInt2Oct(self):

        """Testing converting integer number to octal

        Parameters:
        value (integer): 10

        Returns:
        string: 0o12

        """

        self.assertEqual(int2Oct(10), '0o12')

    # Test bin2Oct function
    def testBin2Oct(self):

        """Testing converting binary number to octal.

        Parameters:
        value (binary): 0b1010

        Returns:
        string: 0o12

        """

        self.assertEqual(bin2Oct(0b1010), '0o12')

    # Test oct2Hex function
    def testOct2Hex(self):

        """Testing converting octal number to hexadecimal.

        Parameters:
        value (octal): 0o12

        Returns:
        string: 0xa

        """

        self.assertEqual(oct2Hex(0o12), '0xa')

    # Test int2Hex function
    def testInt2Hex(self):

        """Testing converting integer number to hexadecimal

        Parameters:
        value (octal): 10

        Returns:
        string: 0xa

        """

        self.assertEqual(int2Hex(10), '0xa')

    # Test bin2Hex function
    def testBin2Hex(self):

        """Testing converting binary number to hexadecimal.

        Parameters:
        value (binary): 0b1010

        Returns:
        string: 0xa

        """

        self.assertEqual(bin2Hex(0b1010), '0xa')

    # Test oct2Bin function
    def testOct2Bin(self):

        """Testing converting octal number to binary.

        Parameters:
        value (octal): 0o12

        Returns:
        string: 0b1010

        """

        self.assertEqual(oct2Bin(0o12), '0b1010')

    # Test int2Bin function
    def testInt2Bin(self):

        """Testing converting integer number to binary.

        Parameters:
        value (integer): 10

        Returns:
        string: 0b1010

        """

        self.assertEqual(int2Bin(10), '0b1010')

    # Test hex2Bin function
    def testHex2Bin(self):

        """Testing converting hexadecimal number to binary.

        Parameters:
        value (hexadecimal): 0xa

        Returns:
        string: 0b1010

        """

        self.assertEqual(hex2Bin(0xa), '0b1010')

if __name__ == '__main__':
    unittest.main()

