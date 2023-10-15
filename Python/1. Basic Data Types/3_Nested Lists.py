# Given the names and grades for each student in a class of students, store them in a nested list and print the name(s)
# of any student(s) having the second lowest grade.

if __name__ == '__main__':
    score_rec = []
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_rec.append(score)
        records.append([name, score])

    sec_low_names = []
    sec_low = min([i for i in score_rec if i != min(score_rec)])
    for i in range(len(records)):
        if score_rec[i] == sec_low:
            sec_low_names.append(records[i][0])
    sec_low_names.sort()
    for i in sec_low_names:
        print(i)
