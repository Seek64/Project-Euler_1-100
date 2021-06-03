# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 09:50:42 2018

@author: Lucas Deutschmann
"""

from sympy import sieve
from math import floor, log

# Initialization
N = 20
result = 1

# Calculate result by continuously multiplying the highest multiple of each prime lower than N
for prime in sieve.primerange(1, N+1):
    result *= prime ** floor(log(N, prime))

# Print result
print(result)