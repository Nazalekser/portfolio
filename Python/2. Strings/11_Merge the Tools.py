# We can split s into n/t substrings where each subtring, consists of a contiguous block of
#  characters in s. Then, use each to create string u such that:
#
# - The characters in u are a subsequence of the characters in t
# - Any repeat occurrence of a character is removed from the string such that each character u in
# occurs exactly once.

def merge_the_tools(string, k):
    # your code goes here
    n = int(len(string)/k)
    res = [''] * n
    a = [string[i:i + k] for i in range(0, len(string), k)]
    for i in range(n):
        for j in range(k):
            if string[i*k+j] in a[i]:
                res[i] += string[i*k+j]
                a[i] = a[i].replace(string[i*k+j], '')
    for i in res:
        print(i)

    # print(*(''.join(dict.fromkeys(string[i: i + k])) for i in range(0, len(string), k)), sep='\n')

    # for x in range(len(string) // k):
    #     res = []
    #     for letter in string[x * k: x * k + k]:
    #         if letter not in res:
    #             res.append(letter)
    # print(''.join(res))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
