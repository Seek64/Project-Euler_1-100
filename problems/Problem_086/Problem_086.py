# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 09:35:57 2018

@author: Lucas Deutschmann
"""

from math import gcd, sqrt

# Input: A Pythagorean pair (a, b) with a < b and a maximum edge size M
# Output: Number of possible cuboids n with a shortest path of c = sqrt(a*a+b*b)
def CalculateDistinctCuboids(a, b, M):
        
    n = 0
    if (b <= M):
        n += a//2
        
    if (a <= M) and (2*a >= b):
        if (b%2 == 0):
            n += a - (b//2) + 1
        else:
            n += a - (b//2)
         
    return n

# Initialization
M = 1818
result = 0
n_max = int(sqrt(M))

# Compute Pythagorean triples with Euclid's formula:
# a = m*m - n*n
# b = 2*m*n
# m > n
# m and n are coprime and not both odd
for m in range(2, M):
    
    # Ensure that not both are odd
    if (m % 2 == 0):
        n = 1
    else:
        n = 2
        
    # Ensure m > n
    while n < m and n < n_max:
        
        # Check if coprime
        if (gcd(m,n) == 1):
            a = m*m - n*n
            b = 2*m*n
            
            # Let a < b
            if (a > b):
                temp = a
                a = b
                b = temp
            
            # Check if result lies in boundary
            if (a <= M and b <= 2*M):
                
                # Go through all multiples of the primitive pair
                for k in range(1, (M//a)+1):
                    result += CalculateDistinctCuboids(k*a, k*b, M)
        
        n += 2
    
# Used binary search manually to find the appropriate M
print(M, result)