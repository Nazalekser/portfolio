from itertools import product

# K, M = map(int, input().split())
# N = {}
# for i in range(K):
#     N[i] = list(map(int, input().split()))[1:]
# S = -1

# for comb in list(product(*N.values())):
#     S = max(S, sum(i*i for i in comb) % M)

# print(S)

k, m = map(int, input().split())
lists = [list(map(int, input().split()))[1:] for _ in range(k)]
print(lists)

max_val = -1
for values in product(*lists):
    max_val = max(max_val, sum(v**2 for v in values) % m)

print(max_val)
