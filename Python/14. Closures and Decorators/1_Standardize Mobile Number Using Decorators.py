'''
The given mobile numbers may have +91, 91 or 0 written before the actual digit number. 
Alternatively, there may not be any prefix at all.
To solve the above question, make a list of the mobile numbers and pass it to a function
that sorts the array in ascending order. Make a decorator that standardizes the mobile 
numbers and apply it to the function. '''


def wrapper(f):
    def fun(l):
        # complete the function
        l = [f'+91 {i[-10:-5]} {i[-5:]}' for i in l]
        f(l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 