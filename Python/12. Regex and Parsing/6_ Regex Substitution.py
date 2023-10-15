# You are given a text of N lines. The text contains && and || symbols.
# Your task is to modify those symbols to the following:
# && → and
# || → or

import re

for i in range(int(input())):
    string = re.sub(r'(?<=\s)\&\&(?=\s)', r'and', input())
    string = re.sub(r'(?<=\s)\|\|(?=\s)', r'or', string)
    print(string)

# for i in range(int(input())):
#   print(re.sub(r"(?<=\s)\|{2}(?=\s)",'or',re.sub(r"(?<=\s)&&(?=\s)",'and',input())))

# for _ in range(int(input())):
#     print(re.sub(r" \|\|(?= )", " or", re.sub(r" &&(?= )", " and", input())))
