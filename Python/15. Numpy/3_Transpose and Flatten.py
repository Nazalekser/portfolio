'''You are given a MxN integer array matrix with space separated elements (N = rows and M = columns).
Your task is to print the transpose and flatten results.'''

import numpy as np

n = input().strip().split()[0]
arr = []
for _ in range(int(n)):
    arr.append(list(map(int, input().strip().split())))

print(np.transpose(arr))
print(np.array(arr).flatten())


# n, m = map(int, input().split())
# a = np.array([list(map(int, input().split())) for _ in range(n)])
# print(a.T)
# print(a.flatten())
