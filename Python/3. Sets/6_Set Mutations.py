# Input Format

# The first line contains the number of elements in set A.
# The second line contains the space separated list of elements in set A.
# The third line contains integer N, the number of other sets.
# The next 2*N lines are divided into N parts containing two lines each.
# The first line of each part contains the space separated entries of the operation name and the length of the other set.
# The second line of each part contains space separated list of elements in the other set.

# Output Format

# Output the sum of elements in set A.

n = int(input())
A = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    c = list(input().split())
    B = set(map(int, input().split()))
    if c[0] == 'update':
        A.update(B)
    elif c[0] == 'intersection_update':
        A.intersection_update(B)
    elif c[0] == 'difference_update':
        A.difference_update(B)
    elif c[0] == 'symmetric_difference_update':
        A.symmetric_difference_update(B)

print(sum(A))