import re
text = []
pattern1 = r'\{([^}]*)\}'
pattern2 = r'#[\dA-Fa-f]{3}(?=[^\dA-Fa-f])|#[\dA-Fa-f]{6}'

for _ in range(int(input())):
    text.append(input())

for i in re.findall(pattern1, ''.join(text)):
    for j in re.findall(pattern2, i):
        print(j)

'''
for _ in range(int(input())):
    rslt = re.findall(r'(?<=.)(#[\da-fA-F]{6}|#[\da-fA-F]{3})', input())
    if rslt: print(*rslt, sep='\n')'''

'''
for _ in range(int(input()):
    match = re.findall(r'\#[a-fA-F0-9]{3,6}(?=[;,)])', input())
    if match:
        print(*match, sep='\n')'''