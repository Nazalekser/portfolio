# You are the manager of a supermarket. 
# You have a list of N items together with their prices that consumers bought on a particular day.
# Your task is to print each item_name and net_price in order of its first occurrence.

from collections import OrderedDict as od
from collections import OrderedDict
lst = OrderedDict()

n = int(input())
for i in range(n):
    parts = input().split()
    item_name, price = ' '.join(parts[:-1]), int(parts[-1])
    if item_name in lst:
        lst[item_name] += int(price)
    else:
        lst[item_name] = int(price)
for key, value in lst.items():
    print(key, value)


# d = OrderedDict()
# for _ in range(int(input())):
#     name, price = input().rsplit(' ', 1)
#     d.setdefault(name, [0])[0] += int(price)
# [print(f'{n} {p[0]}') for n, p in d.items()]


# n = int(input())
# dic = od()
# for i in range(n):
#     product, price = input().rsplit(' ', 1)
#     dic[product] = int(price) + dic.get(product, 0)
# print(*(f"{k} {v}" for k, v in dic.items()), sep='\n')
