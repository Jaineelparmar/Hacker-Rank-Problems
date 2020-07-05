import numpy as np
N, M = map(int, input().split())
x = np.array([list(map(int,input().split())) for _ in range(N)])
y = np.array([list(map(int,input().split())) for _ in range(N)])
print(x+y)
print(x-y)
print(x*y)
print(x//y)
print(x%y)
print(x**y)



