"""
Author: Lucas Deutschmann

Date: 2021-09-15
"""

N = 1001
result = 1

"""
We get the value of one ring by multiplying the number k left to the center by 4
k follows the sequence 1, 6, 19, 40, 69..., i.e., k = (2i)^2+i
"""
for i in range(N//2):
    result += 4 * (4 * i ** 2 + i)

print(result)
