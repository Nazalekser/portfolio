# A valid mobile number is a ten digit number starting with a 7, 8 or 9. 

import re
for _ in range(int(input())):
    print('YES' if bool(re.match(r'^(7|8|9)\d{9}$', input())) else 'NO')


# print(*['YES' if bool(re.match(r'^[789]\d{9}$', input()))
#       else 'NO' for _ in range(int(input()))], sep='\n')
