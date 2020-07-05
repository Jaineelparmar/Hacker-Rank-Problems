def average(array):
    x = set(array)
    return sum(x)/len(x)
    

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)