# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 10:42:54 2018

@author: Lucas Deutschmann
"""

# Checks if a given integer n is palindromic
def IsPalindromic(n):
    
    # Get string representation of number and its length
    n_repr = repr(n)
    n_len = len(n_repr)
    
    # Take first half of number-string
    n_1 = n_repr[0:n_len//2]
    
    # Take reversed second half of number string
    n_2 = n_repr[n_len:(n_len-1)//2:-1]
    
    # Compare
    if (n_1 == n_2):
        return True
    else:
        return False
    

# Initialization
result = 0

# Compute result
for i in range(100, 1000):
    for j in range(i, 1000):
        
        n = i * j
        
        if (n > result) and IsPalindromic(n):
            result = n
            
# Print result
print(result)
    

