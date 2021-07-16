"""
Author: Lucas Deutschmann

Date: 2021-07-16
"""

from math import factorial

# Python supports arbitrary precision Integers
result = sum([int(n) for n in str(factorial(100))])

print(result)
