"""
@author: Lucas Deutschmann
"""

# A pythagorean triplet is generated by the following terms
# a = u*u - v*v
# b = 2*u*v
# c = u*u + v*v
# where u > v > 0

# From a + b + c = 1000, we can deduce v = 500/u - u, where u > v > 0

# Iterate over possible values for u
u, v = 0, 0
for u in range(1, 501):
    if 500 % u == 0:
        v = 500 // u - u
        if u > v > 0:
            break

# Calculate result
a = u*u - v*v
b = 2*u*v
c = u*u + v*v
result = a * b * c

print(result)
