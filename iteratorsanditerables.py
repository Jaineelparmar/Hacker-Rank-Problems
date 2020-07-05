from itertools import combinations
N = int(input())
L = input().split()
M = int(input())
C = list(combinations(L, M))
F = filter(lambda c: 'a' in c, C)
print(len(list(F))/len(C))