# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 18:34:09 2018

@author: Lucas Deutschmann
"""

from math import gcd, sqrt

# Initialization
MAX_PERIMETER = 10**9
MAX_C = (MAX_PERIMETER+1) // 3
MAX_A = (MAX_C+1)//2
MAX_M = (int) (sqrt(MAX_C))
result = 0

# Use Euclid's formula for generating possible Pythagorean triples
# We look for triples with the following property:
# abs(2a-c) = 1 or abs(2b-c)=1
for m in range(2, MAX_M):

    # Calculate all possibilities
    n_1 = (int) (sqrt(((m*m+1))/3))  # derived from "abs(2a-c) = 1"
    n_2 = (int) (sqrt(((m*m-1))/3))  # derived from "abs(2a-c) = 1"
    n_3 = 2*m - (int)(sqrt(3*m*m+1)) # derived from "abs(2b-c) = 1"
    n_4 = 2*m - (int)(sqrt(3*m*m+1)) # derived from "abs(2b-c) = 1"


    for n in {n_1, n_2, n_3, n_4}:
        
        # One needs to be odd and one even
        if (m%2) != (n%2):
            
            # m and n need to be coprime
            if (gcd(m, n) == 1):
                
                # Generate the triple
                a = m*m-n*n
                b = 2*m*n
                c = m*m+n*n
    
                # Let a < b
                if (a > b):
                    a, b = b, a
    
                # Check if a matching triangle is found and increment result
                if (c <= MAX_C) and (a <= MAX_A) and (abs(2*a-c) == 1):
                    result += (2 *(a+c))  

# Print result
print(result)