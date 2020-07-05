for i in range(int(input())):
    x = input()
    if (x.isdigit()) and (len(x) == 10) and (x[0] == '7' or x[0] == '8' or x[0] == '9'):
        print('YES')
    else:
        print('NO')


#OR


import re
for i in range(int(input())):
    if re.match(r'[789]\d{9}$', input()):
        print('YES')
    else:
        print('NO')