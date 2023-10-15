'''
A valid email address meets the following criteria:
    - It's composed of a username, domain name, and extension assembled in this format: 
        username@domain.extension
    - The username starts with an English alphabetical character, and any subsequent characters
        consist of one or more of the following: alphanumeric characters, -,., and _.
    - The domain and extension contain only English alphabetical characters.
    - The extension is 1, 2, or 3 characters in length.
Given n pairs of names and email addresses as input, print each name and email address pair 
    having a valid email address on a new line.

    Hint: Try using Email.utils() to complete this challenge.
'''

import re
for _ in range(int(input())):
    s = input()
    if bool(re.search(r'\<[A-Za-z][\w.-]+@[A-Za-z]+\.[A-Za-z]{1,3}>$', s)):
        print(s)


'''
from re import fullmatch
from email.utils import parseaddr

for _ in range(int(input())):
    s = input()

    if fullmatch(r"[a-zA-Z][a-zA-Z0-9_\-\.]+@[a-zA-Z]+\.[a-zA-Z]{1,3}", parseaddr(s)[1]):
        print(s)
'''


