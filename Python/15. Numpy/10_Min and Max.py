'''You are given a 2-D array with dimensions NxM.
Your task is to perform the min function over axis 1 and then find the max of that.'''

import numpy as np
n, m = map(int, input().split())

a = np.array([input().split() for _ in range(n)], int)

print(np.max(np.min(a, axis=1)))
