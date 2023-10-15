# You are given a list of N lowercase English letters. For a given integer K, you can select any K
# indices (assume-1-based indexing) with a uniform probability from the list. Find the probability
# that at least one of the K indices selected will contain the letter: 'a'. 

from itertools import combinations
N = int(input())
S = input().split()
K = int(input())
p = 0
comb = list(combinations(S, K))
for i in comb:
    if 'a' in i:
        p += 1
print(round(p/len(comb)), 3)


# print(round(sum([1 for i in comb if 'a' in i])/len(comb),3))