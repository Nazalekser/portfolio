'''Neo has a complex matrix script. The matrix script is a N x M grid of strings.
It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).
To decode the script, Neo needs to read each column and select only the alphanumeric
characters and connect them. Neo reads the column from top to bottom and starts reading
from the leftmost column.
If there are symbols or spaces between two alphanumeric characters of the decoded script,
then Neo replaces them with a single space '' for better readability. 
'''

import re


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []
matrix_string = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

for i in range(m):
    for j in range(n):
        matrix_string.append(matrix[j][i])

matrix_string = ''.join(matrix_string)
print(re.sub(r'(?<=[\w\d])[\s!@#$%&]+(?=[\w\d])', ' ', matrix_string))


# matrix_string = "".join(sum(zip(*matrix), ()))
