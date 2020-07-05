from collections import OrderedDict

n = int(input())
d = OrderedDict()

for _ in range(n):
    item = input().split()

    if item[1].isdigit():
        item[1] = int(item[1])
        name = item[0] 
        if d.get(name): 
            d[name] += item[1]
        else:   
            d[name] = item[1]

    else:    
        item[2] = int(item[2])
        name = item[0] + ' ' + item[1]
        if d.get(name): 
            d[name] += item[2]
        else:   
            d[name] = item[2]
        
for x, y in d.items():
    print(x, y)
