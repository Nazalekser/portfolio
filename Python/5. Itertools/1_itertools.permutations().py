# You are given a string S.
# Your task is to print all possible permutations of size k of the string in lexicographic sorted order.


from itertools import permutations
S, k = input().split()
lst = list(permutations(sorted(S), int(k)))
for i in range(len(lst)):
    print(''.join(lst[i]))

# print(*results,sep='\n')
# print("\n".join(results))

# from itertools import permutations
# s,k = input().split()
# print('\n'.join(sorted([''.join(i) for i in permutations(s,int(k))])))