cube = lambda x: pow(x, 3)

def fibonacci(n):
    li = []
    f1 = 0
    f2 = 1
    c = 2
    if n == 1:
        li.append(f1)
    elif n == 2:
        li.append(f1)
        li.append(f2)
    elif n > 2:
        li.append(f1)
        li.append(f2)
        while c < n:
            f = f1+f2
            li.append(f)
            f1, f2 = f2, f
            c += 1
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


#OR

cube = lambda x: pow(x, 3)

def fibonacci(n):
    li =[0, 1]
        for i in range(2, n):
            li.append(li[i-2] + li[i-1])
        return(li[0:n])

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))