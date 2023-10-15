# Task

# Perform append, pop, popleft and appendleft methods on an empty deque d

# Input Format

# The first line contains an integer N, the number of operations.
# The next N lines contains the space separated names of methods and their values.

# Output Format
# Print the space separated elements of deque d.

from collections import deque
d = deque()
N = int(input())

for _ in range(N):
    command = list(input().split())
    if command[0]=='pop':
        d.pop()
    elif command[0] == 'popleft':
        d.popleft()
    elif command[0] == 'append':
        d.append(command[1])
    elif command[0] == 'appendleft':
        d.appendleft(command[1])
print(*d)

# from collections import deque
# dequeue = deque()

# for _ in range(int(input())):
#     command, *args = input().split()
#     getattr(dequeue, command)(*args)

# print(*dequeue)
