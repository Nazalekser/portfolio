'''You are given two arrays A and B. Both have dimensions of NxN.
Your task is to compute their matrix product.'''

import numpy as np
n = int(input())

a = np.array([input().split() for _ in range(n)], int)
b = np.array([input().split() for _ in range(n)], int)

print(np.dot(a, b))
