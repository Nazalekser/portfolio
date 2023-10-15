# You are given a string S. Your task is to print all possible combinations, up to size k, of 
# the string in lexicographic sorted order.

from itertools import combinations
S, k = input().split()
lst = []
for i in range(1, int(k)+1):
    lst.append(list(combinations(sorted(S), i)))
for i in lst:
    print('\n'.join(''.join(j) for j in i))



# from itertools import combinations
# string,value = input().split()

# [print('\n'.join(''.join(val) for val in combinations(sorted(string),ite))) for ite in range(1,int(value)+1)]

# from itertools import combinations_with_replacement # another tool!
