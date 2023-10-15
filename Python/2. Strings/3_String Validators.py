# Python has built-in string validation methods for basic data. It can check if a string is
# composed of alphabetical characters, alphanumeric characters, digits, etc.

if __name__ == '__main__':
    s = input()
    result = False
    for i in range(len(s)):
        if s[i].isalnum():
            result = True
            break
    print(result)

    result = False
    for i in range(len(s)):
        if s[i].isalpha():
            result = True
            break
    print(result)

    result = False
    for i in range(len(s)):
        if s[i].isdigit():
            result = True
            break
    print(result)

    result = False
    for i in range(len(s)):
        if s[i].islower():
            result = True
            break
    print(result)

    result = False
    for i in range(len(s)):
        if s[i].isupper():
            result = True
            break
    print(result)

    # list_convert = list(s)
    #
    # alnum = False
    # alpha = False
    # digit = False
    # lower = False
    # upper = False
    #
    # for i in list_convert:
    #     alpha = alpha or i.isalpha()
    #     digit = digit or i.isdigit()
    #     lower = digit or i.islower()
    #     upper = digit or i.isupper()
    #
    # alnum = alpha and digit
    #
    # print(f"{album}\n{alpha}\n{digit}\n{lower}\n{upper}")
