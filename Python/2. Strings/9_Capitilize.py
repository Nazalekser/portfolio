def solve(s):
    list_s = s.split()
    for i in range(len(list_s)):
        s = s.replace(list_s[i], list_s[i].capitalize())
    return s


if __name__ == '__main__':
    string = input()
    print(solve(string))
