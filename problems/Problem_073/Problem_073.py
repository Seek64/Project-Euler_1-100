# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 17:03:35 2018

@author: Lucas Deutschmann
"""

from math import gcd

# Initialization
result = 0

# Calculate result 
for n in range(2, 12001):
    
    # Find starting and ending point of fraction sequence
    i = n//3 + 1
    i_end   = (n-1)//2
    
    while i <= i_end:
        
        # If it is a proper fraction, increment result
        if gcd(i, n) == 1:
            result += 1
            
        i += 1
    
# Print result
print(result)