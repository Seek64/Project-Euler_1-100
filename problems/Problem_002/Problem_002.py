# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 19:16:43 2018

@author: Lucas Deutschmann
"""

# Initialization
a0 = 1
a1 = 2
result = 0

# For all fibonacci numbers smaller than 4 million
while a1 < 4000000:
    
    # Check if current number is even
    if a1 % 2 == 0:
        result += a1
        
    # Calculate next fibonacci number
    temp = a1
    a1 = a1 + a0
    a0 = temp
    
    
# Print result
print(result)