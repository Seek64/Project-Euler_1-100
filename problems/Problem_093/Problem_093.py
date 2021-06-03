# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 20:01:42 2018

@author: Lucas Deutschmann
"""

# Computes all arithmetic combinations of n with every element of L
def GetCombinations(n, L):
    
    R = set()
    
    for a in L:
        R.add(n+a)
        
        R.add(abs(n-a))
            
        R.add(n*a)
        
        if (n != 0):
            k = a/n
            R.add(k)
            if ((k).is_integer()):
                R.add(a//n)
        if (a != 0):
            k = n/a
            R.add(k)
            if ((k).is_integer()):
                R.add(n//a)
            
    return R

# Recursive algorithm
# Input: List N with up to 4 integer numbers
# Output: Set C of all possible numbers, which can be expressed by N
def ArithmeticExpressions(N):
    
    # Recursion end
    if (len(N) == 1):
        return set(N)
    else:
        C = set()
        
        # Recursively compute all combinations of n with N/n
        for n in N:
            N_red = list(N)
            N_red.remove(n)
            C |= GetCombinations(n, ArithmeticExpressions(N_red))
            
        # Combinations like (a+b)*(c+d) are to be covered
        if (len(N) == 4):
            AB = ArithmeticExpressions([N[0], N[1]])
            CD = ArithmeticExpressions([N[2], N[3]])
            for n in AB:
                C |= GetCombinations(n, CD)
            AC = ArithmeticExpressions([N[0], N[2]])
            BD = ArithmeticExpressions([N[1], N[3]])
            for n in AC:
                C |= GetCombinations(n, BD)
            AD = ArithmeticExpressions([N[0], N[3]])
            BC = ArithmeticExpressions([N[1], N[2]])
            for n in AD:
                C |= GetCombinations(n, BC)
            
    return C

# Computes the length of the sequence of natural numbers in C
def CheckLength(C):
    i = 1
    while i in C:
        i += 1
    return (i-1)

# Initialization
best = 0

# Iterate over all possible values, saving the best result
for a in range(1, 10):
    for b in range(a+1, 10):
        for c in range(b+1, 10):
            for d in range(c+1, 10):
                C = ArithmeticExpressions([a, b, c, d])
                C_len = CheckLength(C)
                if (best < C_len):
                    best = C_len
                    result = [a, b, c, d]

# Print result
print(result)































