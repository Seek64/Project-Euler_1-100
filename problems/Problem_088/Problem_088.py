# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 06:53:38 2018

@author: Lucas Deutschmann
"""

from numpy import prod

# Initialization
N = 12000
N_2 = 2*N
P = [0, 0]
for p in range(2, N+1):
    P.append(2*p)
    
# Number of factors >1 
a = 2


while 2**a <= N_2:
    
    # Build list of factors >1
    L = [2]*a   
    
    while True:

        # Manage increase of factors
        if (prod(L) >= N_2):
            L[1] += 1
            L[0] = L[1]
            i = 2
            while (prod(L) > N_2) and (L[0] != L[a-1]):
                L[i] += 1
                for j in range(0, i):
                    L[j] = L[i]
                i += 1
                
        # Calculate product of factors
        L_prod = prod(L)
        
        # Check if all possibilities for a are checked
        if (L_prod >= 2*N) and (L[0] == L[a-1]):
            break
        
        # Calculate number of all factors and their product
        k = a + L_prod - sum(L)
        f_k = L_prod
        
        # Check if better solution is found
        if (k <= N) and (f_k < P[k]):
            P[k] = f_k
            
        # Inrement last factor
        L[0] += 1
        
    # Increment number of factors >1
    a += 1

# Calculate sum of unique elements
result = sum(set(P[2:]))

# Print result
print(result)