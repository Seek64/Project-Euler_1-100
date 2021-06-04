"""
Author: Lucas Deutschmann

Date: 2020-06-03
"""


def collatz_len(n):
    seq_len = 1
    while n > 1:
        n = ((n // 2) if ((n % 2) == 0) else (n * 3 + 1))
        seq_len += 1
    return seq_len


N = 1000000
max_n = 1
max_seq = 1

for i in range(N):
    if collatz_len(i) > max_seq:
        max_n = i
        max_seq = collatz_len(i)

print(max_n)