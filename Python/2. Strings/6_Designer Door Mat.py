# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door
# mat with the following specifications:
# Mat size must be NxM. (N is an odd natural number, and M is 3 times N .)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.

N, M = map(int, input().split())
c = '.|.'
for i in range(N//2):
    print((c*(2*i+1)).center(M, '-'))
print('WELCOME'.center(M, '-'))
for i in range(N//2):
    print((c*(N - (2*i+2))).center(M, '-'))
