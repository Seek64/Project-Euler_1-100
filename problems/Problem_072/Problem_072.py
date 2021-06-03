# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 16:56:47 2018

@author: Lucas Deutschmann
"""

from sympy.ntheory import totient

# Initialization
result = 0

# Calculate result using Euler's totient function
for n in range(2, 1000001):
    result += totient(n)
    
# Print result
print(result)
