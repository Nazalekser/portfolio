'''You are given a space separated list of numbers.
Your task is to print a reversed NumPy array with the element type float.'''

import numpy


def arrays(arr):
    return numpy.array(arr[::-1], float)


arr = input().strip().split(' ')
result = arrays(arr)
print(result)