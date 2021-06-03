# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 18:45:23 2018

@author: Lucas Deutschmann
"""

from math import sqrt, ceil, floor

# Empiric observation: 
# Ratio of the total number of discs d approaches S = 5.82842...
S = 2 * (1+sqrt(2)) + 1
d = 4   

# Calculate until d > 10**12
while(d < 10**12):
    d = floor(d*S) - 2
    
# Get number of blue discs
n = ceil(d/sqrt(2))
    
# Print solution
print(n)