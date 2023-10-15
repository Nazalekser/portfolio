# In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat,
# in word group A. There are m words belonging to word group B. For each m words, check whether 
# the word has appeared in group A or not. Print the indices of each occurrence of m in group A. 
# If it does not appear, print -1.

from collections import defaultdict

d = defaultdict(list)
n, m = map(int, input().split())
for _ in range(n):
    d['A'].append(input())
for i in range(m):
    d['B'].append(input())
    lst = []
    for j in range(n):
        if d['B'][i]==d['A'][j]:
            lst.append(d['A'].index(d['B'][i], j) + 1)
    print(*lst if lst else [-1])

# from collections import defaultdict

# n,m = map(int, input().split())
# d = defaultdict(list)
# for i in range(n):
#     d[input()].append(i+1) 

# for _ in range(m):
#     print(*d.get(input(),[-1]))
