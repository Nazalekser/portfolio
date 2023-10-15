#  The string S contains alphanumeric characters only.
# Your task is to sort the string in the following manner:
    # All sorted lowercase letters are ahead of uppercase letters.
    # All sorted uppercase letters are ahead of digits.
    # All sorted odd digits are ahead of sorted even digits.

s = input()
s_low = ''; s_up = ''; s_even = ''; s_odd = ''
for i in s:
    if i.islower():
        s_low += i
    elif i.isupper():
        s_up += i
    elif int(i) % 2 == 1:
        s_odd += i
    else:
        s_even += i
print(''.join(sorted(s_low)) + ''.join(sorted(s_up)) + ''.join(sorted(s_odd)) + ''.join(sorted(s_even)))


# chars = sorted(input())
# chars.sort(key=lambda x: (x.isdigit(), x.isupper(), x.islower(), x in "24680"))
# print(*chars, sep="")

# s = list(input())
# s.sort(key=lambda x: (x in '02468', x.isdigit(), x.isupper(), x.islower(), x))
# print(*s, sep='')


# print(*sorted(input(), key=lambda x: (x in '02468', x.isdigit(), x.isupper(), x.islower(), x)), sep='')
