'''You are given a space separated list of nine integers. 
Your task is to convert this list into a 3X3 NumPy array.'''

import numpy as np

arr = input().strip().split(' ')
print(np.reshape(np.array(arr, int), (3, 3)))
