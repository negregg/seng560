#!/usr/bin/python3

import math

# Adds two values and returns a result
def addValue(value1, value2):
    if isinstance(value1, (str, complex, bool)):
        raise Exception('value1 should must be of type integer or float')
    if isinstance(value2, (str, complex, bool)):
        raise Exception('value2 should must be of type integer or float.')
    result = value1 + value2
    return result

# Substracts two values and returns a result
def subValue(value1, value2):
    if isinstance(value1, (str, complex, bool)):
        raise Exception('value1 should must be of type integer or float')
    if isinstance(value2, (str, complex, bool)):
        raise Exception('value2 should must be of type integer or float.')
    result = value1 - value2
    return result

# Multiplies two values and returns a result
def multiValue(value1, value2):
    if isinstance(value1, (str, complex, bool)):
        raise Exception('value1 should must be of type integer or float')
    if isinstance(value2, (str, complex, bool)):
        raise Exception('value2 should must be of type integer or float.')
    result = value1 * value2
    return result

# Divides value 1 by value 2 and returns the result
def divValue(value1, value2):
    if isinstance(value1, (str, complex, bool)):
        raise Exception('value1 should must be of type integer or float')
    if isinstance(value2, (str, complex, bool)):
        raise Exception('value2 should must be of type integer or float.')
    result = value1 / value2
    return result

# Finds square root of a value
def sqrtValue(value):
    if isinstance(value, (str, complex, bool)):
        raise Exception('value should must be of type integer or float')
    math.sqrt(value);
    return result

# Find exponent value ( i.e. value1^(value2))
def expValue(value1, value2):
    if isinstance(value1, (str, complex, bool)):
        raise Exception('value1 should must be of type integer or float')
    if isinstance(value2, (str, complex, bool)):
        raise Exception('value2 should must be of type integer or float.')
    result = value1 + value2
    return result

# Returns octal value as int
def oct2Int(value):
    if isinstance(value, (str, complex, bool)):
        raise Exception('value should must be of type octal')
    result = int(value)
    return result

# Returns hexadecimal as int
def hex2Int(value):
    if isinstance(value, (str, complex, bool)):
        raise Exception('value should must be of type hex')
    result = int(value)
    return result

# Returns binary as int
def bin2Int(value):
    if isinstance(value, (str, complex, bool)):
        raise Exception('value should must be of type binary')
    result = int(value)
    return result

# Returns hex as oct
def hex2Oct(value):
    if isinstance(value, (str, complex, bool)):
        raise Exception('value should must be of type hexadeciman')
    result = oct(value)
    return result

# Returns int as oct
def int2Oct(value):
    if isinstance(value, (str, complex, bool)):
        raise Exception('value should must be of type integer')
    result = oct(value)
    return result

# Returns bin as oct
def bin2Oct(value):
    if isinstance(value, (str, complex, bool)):
        raise Exception('value should must be of type binary')
    result = oct(value)
    return result

# Returns oct as hex
def oct2Hex(value):
    if isinstance(value, (str, complex, bool)):
        raise Exception('value should must be of type octal')
    result = hex(value)
    return result

# Returns int as hex
def int2Hex(value):
    if isinstance(value, (str, complex, bool)):
        raise Exception('value should must be of type integer')
    result = hex(value)
    return result

# Returns bin as hex
def bin2Hex(value):
    if isinstance(value, (str, complex, bool)):
        raise Exception('value should must be of type binary')
    result = hex(value)
    return result

# Returns oct as bin
def oct2Bin(value):
    if isinstance(value, (str, complex, bool)):
        raise Exception('value should must be of type octal')
    result = bin(value)
    return result

# Returns int as bin
def int2Bin(value):
    if isinstance(value, (str, complex, bool)):
        raise Exception('value should must be of type integer')
    result = bin(value)
    return result

# Returns hex as bin
def hex2Bin(value):
    if isinstance(value, (str, complex, bool)):
        raise Exception('value should must be of type hexadecimal')
    result = bin(value)
    return result
