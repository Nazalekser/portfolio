# Consider a list (list = []). You can perform the following commands:
#
# 1. insert i e: Insert integer at position i
# 2. print: Print the list.
# 3. remove e: Delete the first occurrence of integer
# 4. append e: Insert integer at the end of the list.
# 5. sort: Sort the list.
# 6. pop: Pop the last element from the list.
# 7. reverse: Reverse the list.

# Initialize your list and read in the value of followed by lines of commands where each command
# will be of the types listed above. Iterate through each command in order and perform the
# corresponding operation on your list.

if __name__ == '__main__':
    N = int(input())
    my_list = []
    for i in range(N):
        command, *line = input().split()
        if command == 'insert':
            i, e = list(map(int, line))[0], list(map(int, line))[1]
            my_list.insert(i, e)
        elif command == 'print': print(my_list)
        elif command == 'remove': e = list(map(int, line))[0]; my_list.remove(e)
        elif command == 'append': e = list(map(int, line))[0]; my_list.append(e)
        elif command == 'sort': my_list.sort()
        elif command == 'pop': my_list.pop()
        elif command == "reverse": my_list.reverse()

# i, e = int(line[0]), int(line[1])