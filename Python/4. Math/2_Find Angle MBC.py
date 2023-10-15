from math import atan, cos, acos, degrees, sqrt

A, B = int(input()), int(input())

MC = sqrt(A*A + B*B) / 2
MCB = atan(A/B)
BM = sqrt(B*B + MC*MC -2*B*MC*cos(MCB))
MBC = acos((B*B + BM*BM - MC*MC) / (2*B*BM))

print(round(degrees(MBC)), chr(176), sep = '')