from itertools import product

K, M = map(int,input().split())
N = []

for _ in range(K):
    N.append(list(map(int,input().split()))[1:])

# map(lambda x: sum(pow(i, 2) for i in x)
# map(lambda x: sum(pow(i, 2) for i in x) % M
# map(lambda x: sum(pow(i, 2) for i in x) % M, product(*N))

Res = list(map(lambda x: sum(pow(i,2) for i in x) % M, product(*N)))
print(Res)
print(max(Res))