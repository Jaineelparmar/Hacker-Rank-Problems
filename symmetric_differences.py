n = int(input())
s1 = set(map(int, input().split()))
n2 = int(input())
s2 = set(map(int, input().split()))
x = s1.difference(s2)
y = s2.difference(s1)
li = []
for i in x:
    li.append(i)
for i in y:
    li.append(i)
for i in sorted(li):
    print(i)