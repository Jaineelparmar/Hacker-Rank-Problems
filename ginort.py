S = input()
x = []
y = []
o = []
e = []
for i in S:
    if i.islower():
        x.append(i)
    elif i.isupper():
        y.append(i)
    elif i.isdigit() and int(i)%2 != 0:
        o.append(i)
    elif i.isdigit() and int(i)%2 == 0:
        e.append(i)

print(''.join(sorted(x)+sorted(y)+sorted(o)+sorted(e)))


#OR 


import re

S = input()

lower = sorted(re.findall('[a-z]', S))
upper = sorted(re.findall('[A-Z]', S))
odd = sorted(re.findall('[13579]', S))
even = sorted(re.findall('[24680]', S))
print(*lower+upper+odd+even, sep='')




