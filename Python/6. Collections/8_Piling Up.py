# There is a horizontal row of n cubes. The length of each cube is given. You need to create a new 
# vertical pile of cubes. The new pile should follow these directions: if cube[i] is on top of cube[j]
# then sideLength[j] >= sideLength[i]. 
# When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. 
# Print Yes if it is possible to stack the cubes. Otherwise, print No.


from collections import deque

for _ in range(int(input())):
    _ = int(input())
    d = deque(map(int, input().split()))
    a = max(d[0], d[-1])
    for _ in range(len(d)):
        if d[0] <= d[-1] <= a:
            a = d.pop()
        elif d[-1] <= d[0] <= a:
            a = d.popleft()
        else:
            break
    print('Yes' if len(d) == 0 else 'No')




