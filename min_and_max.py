import numpy as np
N, M = map(int, input().split())
x = [input().split() for i in range(N)]
arr = np.array(x,int)
print(np.max(np.min(arr, axis=1)))


