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

## Usage

After loading the natemath module, you can simply use any of the functions listed in
the [API Documentation](https://pdoc3.github.io/pdoc/).  All functions take either
one or two input values depending on the operation being performed.  

## Examples

The following are several examples utilizing the natemath module.  Using the 
examples should show how to easily use the functions available in the API
Documentation.  The following shows output using [iPython](https://ipython.org) 
interface to execute functions from the natemath module.

```python
$ ipython
Python 3.6.8 (default, Apr 25 2019, 21:02:35) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.8.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from natemath import * 
   ...:                                                                                                                                              

In [2]: # Example of adding two values 
   ...: print(addValue(10,5))                                                                                                                        
15.0

In [3]: # Example of muliplying two values 
   ...: print(multiValue(10,5))                                                                                                                      
50.0

In [4]: # Example of square a root value 
   ...: print(sqrtValue(9))                                                                                                                          
3.0

In [5]: # Example of finding exponent value 
   ...: print(expValue(3,2))                                                                                                                         
9

In [6]: # Example of translating integer to binary 
   ...: print(int2Bin(10))                                                                                                                           
0b1010

In [7]: # Example of translating binary to octal 
   ...: print(bin2Oct(0b1010)) 
0o12

In [8]: # Example of translating octal to hexadecimal 
   ...: print(oct2Hex(0o12)) 
0xa

In [9]: # Example of translating hexadecimal to integer 
   ...: print(hex2Int(0xa))                                                                                                                          
10


```

## Module Reuseability
This module has been tested to ensure reusablility for other programs.  This 
was accomplished using the following methods:

* Ensuring a standardized return type from all functions.  All operations
functions return "float" even if all inputs are integers.  This is done to 
ensure consistency of output and to lessen confusion of usage.  If at least
one of the input variable is a float, the result will be returned as a float. 
All base translation functions (i.e. int2Bin) values are returned as a "string"
type.

* Ensures proper data type on input values.  If an invalid data type is entered,
(i.e. boolean), the function will raise an error.

* Every function has an associated "unit test" that ensure the accuracy of 
the function.  Users may want to execute the unit test code on their own.  If so,
simply execute `mathtest.py`.  The unit tests are also easily extendible if users
want to add any additional test cases.

