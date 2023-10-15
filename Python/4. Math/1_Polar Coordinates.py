import cmath

z = complex(input())

print(round(abs(z), 3))
print(round(cmath.phase(z), 3))
