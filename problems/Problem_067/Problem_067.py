"""
Author: Lucas Deutschmann

Date: 2021-07-16
"""

f = open("p067_triangle.txt", "r")
M = f.read()

# Transform string into a 2D List of Integers
M = [[int(n) for n in L.split(" ")] for L in M.split("\n") if L != ""]

# Create an empty list to save the maximum paths for each entry
P = [[M[0][0]]]

# Use Dynamic Programming to save the best intermediate results
for l in range(1, len(M)):
    p = []
    for i in range(l+1):
        if i == 0:
            p.append(M[l][i]+P[l-1][i])
        elif i == l:
            p.append(M[l][i]+P[l-1][i-1])
        else:
            p.append(M[l][i]+max(P[l-1][i-1], P[l-1][i]))
    P.append(p)

# Result is the maximum of the last row
result = max(P[-1])

print(result)
