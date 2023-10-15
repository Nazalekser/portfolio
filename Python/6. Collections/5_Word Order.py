# You are given words. Some words may repeat. For each word, output its number of occurrences.
#  The output order should correspond with the input order of appearance of the word. See the sample
#  input/output for clarification.

from collections import Counter
a = []
for _ in range(int(input())):
    a.append(input())

words = Counter(a)
print(len(words))
print(' '.join(map(str, words.values())))


# from collections import Counter
# words = Counter((input() for _ in range(int(input()))))
# print(len(words))
# print(' '.join(map(str, words.values())))


# from collections import Counter
# n = int(input())
# words = Counter([input() for _ in range(n)])
# print(len(words))
# print(*words.values())
