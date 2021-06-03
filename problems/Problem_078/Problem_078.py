# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 18:07:47 2018

@author: Lucas Deutschmann
"""

# Program is based on partition function P(n)

# Initialization
n = 1
P = [1]


# Setup: Pre-calculations of 0.5*k*(3k-1) and 0.5*k*(3k+1) terms
a = 1
b = 2
a_add = 4
b_add = 5
L = [1, 2]

# Calculate all values until solution is found
while True:
    
    # Initialize value vor P(n)
    p = 0
    
    # Setup alternating sign (+ + - - + + - ...)
    s = 1
    s_cnt = 0
    
    # Update list of pre-calculated 0.5*k*(3k-1) and 0.5*k*(3k+1) terms
    if (n > a):
        a += a_add
        b += b_add
        a_add += 3
        b_add += 3
        L.append(a)
        L.append(b)
    
    # Calculate P(n) by adding or substracting P[n-i]
    for i in L:
        if (i <= n):
            p += s * P[n-i]
        else:
            break
        s_cnt = (s_cnt + 1) % 2
        
        # Readjust sign if needed
        if (s_cnt == 0):
            s *= -1
    
    # Check if solution is found 
    p %= 1000000
    if (p == 0):
        break
    
    # Append new intermediate result (mod 1000000)
    P.append(p)
    n += 1
        
# Print result  
print(n)








