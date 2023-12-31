'''A valid postal code P have to fullfil both below requirements:

1. P must be a number in the range from 100000 to 999999 inclusive.
2. P must not contain more than one alternating repetitive digit pair.

Alternating repetitive digits are digits which repeat immediately after the next digit. 
In other words, an alternating repetitive digit pair is formed by two equal digits that have 
just a single digit between them. '''

import re
regex_integer_in_range = r"^(?!0)\d{6}$"  # Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(\d)\1"  # Do not delete 'r'.


P = input()

print(bool(re.match(regex_integer_in_range, P))
      and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
