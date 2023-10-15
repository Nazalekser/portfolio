# There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m
# integers. You like all the integers in set A and dislike all the integers in set B. Your initial
# happiness is 0. For each i integer in the array, if i Є A, you add to your happiness. If i Є B,
# you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness
# at the end.
#
# Note: Since A and B are sets, they have no repeated elements. However, the array might contain
# duplicate elements.

n, m = map(int, input().split())
X = list(map(int, input().split()))
A, B = set(map(int, input().split())), set(map(int, input().split()))
h = 0

for i in X:
    if i in A:
        h += 1
    if i in B:
        h -= 1

print(h)

# print(sum(1 if i in A else -1 if i in b else 0 for i in X))