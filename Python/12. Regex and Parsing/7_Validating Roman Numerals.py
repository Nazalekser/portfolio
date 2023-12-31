'''You are given a string, and you have to validate whether it's a valid Roman numeral. 
If it is valid, print True. Otherwise, print False. 
Try to create a regular expression for a valid Roman numeral.'''

import re

regex_pattern = r"^M{0,3}(D?C{0,3}|CM|CD)(L?X{0,3}|XC|XL)(V?I{0,3}|IX|IV)$"

print(str(bool(re.match(regex_pattern, input()))))


# regex_pattern = r"^M{,3}(D?C{,3}|C[DM])(L?X{,3}|X[LC])(V?I{,3}|I[VX])$"
