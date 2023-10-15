# Your task is to find the first occurrence of an alphanumeric character in s (read from left to right)
# that has consecutive repetitions.


import re
m = re.search(r"([[0-9a-zA-Z])\1", input())
print(m.group(1) if m else "-1")