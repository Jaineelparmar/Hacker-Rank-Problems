from collections import Counter
K = int(input())
n = Counter(input().split())
print(dict(n))
for i in n:
    if n[i] == 1:
        print(i)
