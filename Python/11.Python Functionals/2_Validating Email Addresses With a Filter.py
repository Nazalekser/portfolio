''' 
You are given an integer N followed by N email addresses. Your task is to print a list 
    containing only valid email addresses in lexicographical order.
A valid email address meets the following criteria:
    - It's composed of a username, domain name, and extension assembled in this format: 
        username@domain.extension
    - The username starts with an English alphabetical character, and any subsequent characters
        consist of one or more of the following: alphanumeric characters, -,., and _.
    - The domain and extension contain only English alphabetical characters.
    - The extension is 1, 2, or 3 characters in length.
'''

def fun(s):
    # return True if s is a valid email, else return False

    if len(s.split('@')) == 2 and len(s.split('@')[0]) != 0:
        if len(s.split('@')[1].split('.')) == 2:
            user = list(s.split('@')[0])
            web = list(s.split('@')[1].split('.')[0])
            ex = list(s.split('@')[1].split('.')[1])
        else:
            return False
    else:
        return False

    val_user = all(list(map(lambda x: x.isalnum() or x in '-_', user)))
    val_web = all(list(map(lambda x: x.isalnum(), web)))
    val_ex = all(list(map(lambda x: x.isalpha(), ex))) and len(ex) <= 3

    return val_user * val_web * val_ex


def filter_mail(emails):
    return list(filter(fun, emails))



if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)


# def fun(s):
#     # return True if s is a valid email, else return False
#     i, k = s.find("@"), s.find(".")
#     if k < len(s)-4 or i < 1: return False
#     for x in range(len(s)):
#         if ((x<i or i<x<k) and not (s[x].isalnum() or (s[x] in "-_" and x<i))) \
#         or (k < x and not (s[x].isalpha())):
#             return False

#     return True


# import re
# def fun(s):
#     m = re.fullmatch(r'[-\w]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}', s)
#     return bool(m)
