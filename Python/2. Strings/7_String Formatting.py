# Given an integer, n, print the following values for each i integer from i to n:
#     Decimal
#     Octal
#     Hexadecimal (capitalized)
#     Binary

# The four values must be printed on a single line in the order specified above for each from to .
# Each value should be space-padded to match the width of the binary value of and the values should
# be separated by a single space.

def print_formatted(number):
    # your code goes here
    space_pad = len(str(bin(number))[2:]) + 1
    for i in range(number):
        print(str(i+1).rjust(space_pad-1) +
              oct(i+1)[2:].rjust(space_pad) +
              hex(i+1)[2:].upper().rjust(space_pad) +
              bin(i+1)[2:].rjust(space_pad))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
