import numpy as np
N, M = map(int, input().split())
x = np.array([input().split() for _ in range(N)], int)
print(np.prod(np.sum(x, axis=0), axis=0))
