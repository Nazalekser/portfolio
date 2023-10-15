# The National University conducts an examination of N students in X subjects.
#  Your task is to compute the average scores of each student.

_, x = map(int, input().split())
s = [tuple(map(float, input().split())) for _ in range(x)]
for i in zip(*s):
    print(sum(i)/len(i))


# _, X = input().split()
# for s in zip(*[list(map(float, input().split())) for _ in range(int(X))]):
#     print(f"{sum(s)/len(s):.1f}")


# n,x=map(int,input().split())
# student_marks=[]
# for i in range(x):
#     marks=map(float,input().split())
#     student_marks.append(marks)
# asd=list(zip(*student_marks))
# for _ in asd:
#     print(round(sum(_)/x,2))