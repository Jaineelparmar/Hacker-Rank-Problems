import numpy as np 

def arrays(arr):
    arr = np.array(arr, float)
    arr = arr[::-1]
    return arr

arr = input().strip().split(' ')
print(arrays(arr))