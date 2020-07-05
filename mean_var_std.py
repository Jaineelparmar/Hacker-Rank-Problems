import numpy as np
np.set_printoptions(legacy='1.13')
N, M = map(int, input().split())
arr = np.array([list(map(int, input().split())) for _ in range(N)])
print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(np.std(arr, axis=None))

