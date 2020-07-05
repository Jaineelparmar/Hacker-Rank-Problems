from collections import Counter
li = []
for i in range(int(input())):
    li.append(input())
z = Counter(li)
print(len(z))
print(*z.values())