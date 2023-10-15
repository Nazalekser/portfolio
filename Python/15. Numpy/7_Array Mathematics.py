'''You are given two integer arrays, and of dimensions NxM.
Your task is to perform the following operations:

Add (A+B)
Subtract (A-B)
Multiply (*)
Integer Division (/)
Mod (%)
Power (** )'''



import numpy as np
n, _ = map(int, input().split())
a = np.array([input().split() for _ in range(n)], int)
b = np.array([input().split() for _ in range(n)], int)
print(np.add(a, b))
print(np.subtract(a, b))
print(np.multiply(a, b))
print(np.floor_divide(a, b))    # The same sa python // operator
print(np.mod(a, b))             # The same sa python % operator
print(np.power(a, b))

# rows, cols = map(int, input().split())
# attrs = ['add', 'subtract', 'multiply',
#          'floor_divide', 'mod', 'power']
# a = np.array([input().split() for row in range(rows)], int)
# b = np.array([input().split() for row in range(rows)], int)
# for attr in attrs:
#     print(getattr(np, attr)(a, b))
