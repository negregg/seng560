# Nate's Python Math Module

## Overview

A basic Python 3 Module that performs basic math operations.  This module 
will take in one or two parameters and perform basic math operations or 
base translations based  on the function that is chosen.  This module can
do the following functions.

### Math Operations
* Add two values
* Subtract two values
* Multiply two values
* Divide two values
* Find square root of a value
* Calculate exponent value

### Math base translations
* Transform between various basis, including:
  * Integer
  * Binary
  * Octal
  * Hexadecimal

## API Documentation

All functions in natemath module are documented in API format using 
[PDOC](https://pdoc3.github.io/pdoc/).  Please click following link to access
documentation:

https://negregg.github.io/seng560/

## Examples

The following are several examples utilizing the natemath module.  Using the 
examples should show how to easily use the functions available in the API
Documentation.

```python

#!/usr/bin/python3

from natemath import *

# Example of adding two values
print(addValue(10,5))

# Example of muliplying two values
print(multiValue(10,5))

# Example of square a root value
print(sqrtValue(9))

# Example of finding exponent value
print(expValue(3,2))

# Example of translating integer to binary
print(int2Bin(10))

# Example of translating binary to octal
print(bin2Oct(0b1010))

# Example of translating octal to hexadecimal
print(oct2Hex(0o12))

# Example of translating hexadecimal to integer
print(hex2Int(0xa))

```

## Module Reuseability
This module has been tested to ensure reusablility for other programs.  This 
was accomplished using the following methods:

* Ensuring a stanrdized return type from all functions.  All operations
functions return either a "integer" or "float" depending on input.  If at least
one of the input variable is a float, the result will be returned as a float. 
All base tranlation functions (i.e. int2Bin) values are returned as a "string"
type.

* Every function has an associated "unit test" that ensure the accuracy of 
the function.  Users may want to execute the unit test code on their own.  If so,
simply execute `mathtest.py`.  `mathtest.py` is also easily extendable if users
want to add any additional test cases.

