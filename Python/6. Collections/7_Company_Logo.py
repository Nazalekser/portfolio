# A newly opened multinational brand has decided to base their company logo on the three most common
# characters in the company name. They are now trying out various combinations of company names and 
# logos based on this condition. Given a string s, which is the company name in lowercase letters, 
# your task is to find the top three most common characters in the string.

# Print the three most common characters along with their occurrence count.
# Sort in descending order of occurrence count.
# If the occurrence count is the same, sort the characters in alphabetical order.

# Input Format
# A single line of input containing the string S.

# Output Format
# Print the three most common characters along with their occurrence count each on a separate line.
# Sort output in descending order of occurrence count.
# If the occurrence count is the same, sort the characters in alphabetical order.

from collections import Counter

def logo_comp(s):
    count = Counter(s)
    res = sorted(count.items())
    res = sorted(res, key=lambda x: x[1], reverse=True)[:3]
    [print(*i) for i in res]


if __name__ == '__main__':
    s = input()
    logo_comp(s)


# from collections import Counter
# [print(*i) for i in Counter(sorted(input())).most_common(3)]


# [print(*s) for s in __import__('collections').Counter(sorted(input())).most_common(3)]


# from collections import Counter
# string = Counter(s)
# string = sorted(string.items(), key=lambda x: (-x[1], x[0]))

# for i in list(string)[0:3]:
#     print(*i)

