# Check Tutorial tab to know how to solve.
# You are given a string and width .
# Your task is to wrap the string into a paragraph of width .

import textwrap


def wrap(string, max_width):
    return textwrap.fill(string, max_width)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
