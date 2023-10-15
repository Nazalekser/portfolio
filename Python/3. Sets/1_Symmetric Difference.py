# Given sets of integers, print their symmetric difference in ascending order.

m = int(input())
set1 = set(map(int, input().split()))
n = int(input())
set2 = set(map(int, input().split()))

print(*sorted(set1.difference(set2).union(set2.difference(set1))), sep='\n')

# _, a = input(), set(input().split())
# _, b = input(), set(input().split())