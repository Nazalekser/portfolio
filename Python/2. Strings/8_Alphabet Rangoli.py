def print_rangoli(size):

    def string(length):
        s = ""
        for i in range(length):
            s = s + chr(96 + size - i) + '-'
            if size == 1:
                s = chr(97)
                break
        for i in range(length-1, 0, -1):
            s = s + chr(97 + size - i)
            if i != 1:
                s = s + '-'
        return s

    for j in range(size):
        print(string(j+1).center(4*size-3, '-'))
    for j in range(size-2, -1, -1):
        print(string(j+1).center(4*size-3, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
