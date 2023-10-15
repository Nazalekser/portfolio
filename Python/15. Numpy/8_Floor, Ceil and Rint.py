'''You are given a 1-D array, A. Your task is to print the floor, ceil and rint of all the elements of A. '''


import numpy as np
a = np.array([input().split()], float)
print(np.floor(a))
print(np.ceil(a))
print(np.rint(a))   # rounds to the nearest integer
