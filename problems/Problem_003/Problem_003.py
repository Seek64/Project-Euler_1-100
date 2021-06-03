# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 19:27:48 2018

@author: Lucas Deutschmann
"""

from sympy.ntheory.factor_ import smoothness

# Use sympy function "smoothness", which finds the largest prime factor of a number
result = smoothness(600851475143)[0]

# Print result
print(result)
