# You are given a string S.
# Your task is to find the indices of the start and end of string in S.

import re
S, k = input(), input()
end = 0

res = re.finditer(r"(?={})".format(k), S)
for i in res:
    end = i.start() + len(k) - 1
    print((i.start(), end))
print((-1, -1) if end == 0 else "")


# pattern = f"(?=({k}))"

# for regex in re.finditer(pattern, S):
#     print(f"({regex.start(1)}, {regex.end(1) - 1})")

# if re.search(pattern, S) is None:
#     print("(-1, -1)")
