from collections import Counter

s = input()
c = Counter(sorted(s))
for i in c.most_common(3):
    print(*i) 

