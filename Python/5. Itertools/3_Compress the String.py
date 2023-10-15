# You are given a string S. Suppose a character 'c' occurs consecutively X times in the string. 
# Replace these consecutive occurrences of the character 'c' with (X, c) in the string. 

from itertools import groupby
S = input()

[print((len(list(g)), int(k)), end=' ') for k, g in groupby(S)]
