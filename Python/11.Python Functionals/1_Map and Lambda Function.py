# Print a list on a single line containing the cubes of the first N fibonacci numbers.

def cube(x): return x**3  # complete the lambda function


def fibonacci(n):
    # return a list of fibonacci numbers
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-2] + fib[i-1])
    return fib[:n]


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


# def fibonacci(n):
#     fib = list()
#     x, y = 0, 1
#     for i in range(n):
#         fib.append(x)
#         x, y = y, x + y
#     return fib
