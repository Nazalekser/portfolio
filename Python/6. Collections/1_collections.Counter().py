# R is a shoe shop owner. His shop has number X of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are N number of customers who are willing to pay x(i) amount of money only if they get
# the shoe of their desired size.

# Your task is to compute how much money R earned.

# Input Format

# The first line contains X, the number of shoes.
# The second line contains the space separated list of all the shoe sizes in the shop.
# The third line contains N, the number of customers.
# The next lines contain the space separated values of the shoe size desired by the customer and
# x(i), the price of the shoe.

# Print the amount of money earned by the shop. 

from collections import Counter

X = int(input())
shoe_sizes = list(map(int, input().split()))
N = int(input())
money = 0

for i in range(N):
    size_price = list(map(int, input().split()))
    if size_price[0] in set(shoe_sizes):
        shoe_sizes.remove(size_price[0])
        money += size_price[1]
print(money)

# money = 0
# _ = int(input())
# count = Counter(input().split())
# for _ in range(int(input())):
#     s, p = input().split()
#     for i, j in count.items():
#         if s == i and j != 0:
#             money += int(p)
#             count[i] -= 1
# print(money)


