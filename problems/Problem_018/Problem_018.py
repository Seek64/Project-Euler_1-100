"""
Author: Lucas Deutschmann

Date: 2021-07-16
"""

M ="""75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

# Transform string into a 2D List of Integers
M = [[int(n) for n in L.split(" ")] for L in M.split("\n")]

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
