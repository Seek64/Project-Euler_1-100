# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 17:39:55 2018

@author: Lucas Deutschmann
"""

# Program is based on partition function P(n)

# Initialization
N = 100
P = [1]

# Setup: Pre-calculate 0.5*k*(3k-1) and 0.5*k*(3k+1) terms
a = 1
b = 2
a_add = 4
b_add = 5
L = []
while(a < N or b < N ):
    L.append(a)
    if(b <= N):
        L.append(b)
    a += a_add
    b += b_add
    a_add += 3
    b_add += 3
    

# Calculate all values until N = 100
for n in range(1, 101):
    
    # Initialize value vor P(n)
    p = 0
    
    # Setup alternating sign (+ + - - + + - ...)
    s = 1
    s_cnt = 0
    
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
    
    # Append new intermediate result
    P.append(p)
        
# Print result  
print(P[N]-1)
    