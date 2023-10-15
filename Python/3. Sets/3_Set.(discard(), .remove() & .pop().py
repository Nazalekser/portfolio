# You have a non-empty set s, and you have to execute N commands given in N lines.
# The commands will be pop, remove and discard.
#
# Input Format
# The first line contains integer n, the number of elements in the set s.
# The second line contains n space separated elements of set s. All of the elements are non-negative
# integers, less than or equal to 9.
# The third line contains integer N, the number of commands.
# The next lines contains either pop, remove and/or discard commands followed by their associated value.

# Output Format
# Print the sum of the elements of set s on a single line.

n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    command = input()
    if command == 'pop':
        s.pop()
    else:
        command, index = command.split()
        s.discard(int(index))

print(sum(s))

# n = int(input())
# s = set(map(int, input().split()))
# N = int(input())
#
# for _ in range(N):
#     c = list(input().split())
#     if 'pop' in c[0]:
#         s.pop()
#     elif 'remove' in c[0]:
#         s.remove(int(c[-1]))
#     elif 'discard' in c[0]:
#         s.discard(int(c[-1]))
#
# print(sum(s))
