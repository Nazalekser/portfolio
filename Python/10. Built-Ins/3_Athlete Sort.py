# You are given a spreadsheet that contains a list of N athletes and their details (such as age, height,
# weight and so on). You are required to sort the data based on the th attribute and print the final 
# resulting table. Follow the example given below for better understanding.


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    sorted_arr = sorted(arr, key=lambda x: x[k])
    for row in sorted_arr:
        print(' '.join(map(str, row)))

    # arr.sort(key=lambda x: x[k])
    # for row in arr:
    #     print(*row)


    # import pandas as pd
    # df = pd.DataFrame(arr)
    # print(df.sort_values(str(k)).to_string(header=False, index=False))

