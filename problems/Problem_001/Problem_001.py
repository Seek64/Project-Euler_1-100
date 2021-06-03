"""
Created on Mon Sep  3 19:06:37 2018

@author: Lucas Deutschmann
"""
# Initialization
result = 0

# Iterate over integer below 1000 and sum up multiples of 3 and 5
for n in range(3, 1000):
    if (n%3 == 0) or (n%5 == 0):
        result += n
        
# Print result
print(result)

