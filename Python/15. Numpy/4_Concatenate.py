'''You are given two integer arrays of size NxP and MxP (N & M are rows, and P is the column).
 Your task is to concatenate the arrays along axis 0.'''


import numpy as np

n, m, _ = map(int, input().split())
a = np.array([list(map(int, input().split())) for _ in range(n)])
b = np.array([list(map(int, input().split())) for _ in range(m)])

print(np.concatenate((a, b), axis=0))


# a = np.array([input().split() for _ in range(n)], int)
# b = np.array([input().split() for _ in range(n)], int)