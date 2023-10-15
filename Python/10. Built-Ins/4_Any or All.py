# You are given a space separated list of integers. If all the integers are positive, 
# then you need to check if any integer is a palindromic integer.

n = int(input())
a = list(map(int, input().split()))
print(all([all(i > 0 for i in a), any(str(i) == str(i)[::-1] for i in a)]))