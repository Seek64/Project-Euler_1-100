"""
@author: Lucas Deutschmann
"""

from sympy import sieve

result = sum([i for i in sieve.primerange(1, 2000000)])

print(result)
