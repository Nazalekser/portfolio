# You are given a string S. Your task is to find the first occurrence of an alphanumeric
# character in S (read from left to right) that has consecutive repetitions.

import re
res = re.findall(r'(?i)(?<=[^aeiou])[aeiou]{2,}(?=[^aeiou])', input())
if len(res) > 0:
    [print(i) for i in res]
else:
    print(-1)


# pat = "(?<=[^aeiou])([aeiou]{2,})[^aeiou]"
# res = re.findall(pat, input(), flags=re.I)

# print('\n'.join(res or ['-1']))

