import numpy as np
N, M, P = map(int, input().split())
x = np.array([list(map(int, input().split())) for i in range(N)])
y = np.array([list(map(int, input().split())) for i in range(M)])
print(np.concatenate((x, y), axis = 0))