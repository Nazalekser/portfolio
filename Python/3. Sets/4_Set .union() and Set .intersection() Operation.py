n = int(input())
s1 = set(map(int, input().split()))
b = int(input())
s2 = set(map(int, input().split()))

print(len(s1.union(s2)))

# >>> s = set("Hacker")
# >>> print s.union("Rank")
# set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

# >>> print s.union(set(['R', 'a', 'n', 'k']))
# set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

# >>> print s.union(['R', 'a', 'n', 'k'])
# set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

# >>> print s.union(enumerate(['R', 'a', 'n', 'k']))
# set(['a', 'c', 'r', 'e', (1, 'a'), (2, 'n'), 'H', 'k', (3, 'k'), (0, 'R')])

# >>> print s.union({"Rank":1})
# set(['a', 'c', 'r', 'e', 'H', 'k', 'Rank'])

# >>> s | set("Rank")
# set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])



# >>> s = set("Hacker")
# >>> print s.intersection("Rank")
# set(['a', 'k'])

# >>> print s.intersection(set(['R', 'a', 'n', 'k']))
# set(['a', 'k'])

# >>> print s.intersection(['R', 'a', 'n', 'k'])
# set(['a', 'k'])

# >>> print s.intersection(enumerate(['R', 'a', 'n', 'k']))
# set([])

# >>> print s.intersection({"Rank":1})
# set([])

# >>> s & set("Rank")
# set(['a', 'k'])