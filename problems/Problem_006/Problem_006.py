# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 07:14:09 2018

@author: Lucas Deutschmann
"""

# Initialization
N = 100

# Calculate result
squareOfSum = (((N+1)*N)//2)**2
sumOfSquares = (N*(N+1)*(2*N+1))//6
result = squareOfSum - sumOfSquares

# Print result
print(result)