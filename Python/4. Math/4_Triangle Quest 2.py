'''You are given a positive integer N.
Your task is to print a palindromic triangle of size N.

For example, a palindromic triangle of size 5 is:

1
121
12321
1234321
123454321

You can't take more than two lines. The first line (a for-statement) is already written for you.
You have to complete the code using exactly one print statement. '''


# More than 2 lines will result in 0 score. Do not leave a blank line also
for i in range(1, int(input())+1):
    print((10**i/9)**2)

# for i in range(1, int(input())+1):
#     print(sum(map(lambda x: 10**x, range(0, i)))**2)
