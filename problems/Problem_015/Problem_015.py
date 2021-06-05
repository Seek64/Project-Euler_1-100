"""
Author: Lucas Deutschmann

Date: 2020-06-05
"""


import scipy.special

N = 20

"""
The number of paths to a specific node is shown in the Pascal triangle
Hence, the problem is equivalent to finding a binomial coefficient
"""
print(scipy.special.comb(2*N, N, exact=True))
