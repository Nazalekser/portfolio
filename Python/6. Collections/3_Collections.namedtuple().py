# Dr. John Wesley has a spreadsheet containing a list of student's IDs, marks, class and name.
# Your task is to help Dr. Wesley calculate the average marks of the students 
# (sum of all marks / total students).


from collections import namedtuple
N = int(input())
cols = namedtuple('spreadsheet', input())
print(round((sum([int(cols(*input().split()).MARKS) for _ in range(N)])/N), 2))


# n = int(input())
# m = namedtuple('h', input())
# print('%.2f' % (sum([int(m(*input().split()).MARKS) for i in range(n)])/n))