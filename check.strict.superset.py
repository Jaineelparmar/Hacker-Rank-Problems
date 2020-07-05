a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(a.issuperset(b))

#OR

n = set(map(int, input().split()))
x = int(input())
li = []
for i in range(x):
    a = set(map(int, input().split()))
    li.append(n.issuperset(a))
print(all(li))
