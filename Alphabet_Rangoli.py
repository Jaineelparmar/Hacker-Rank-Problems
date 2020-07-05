def print_rangoli(size):

    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha = alpha[size-1 :: -1]
    print(alpha)

    width = (size*4) -  3
    print(width)

    x = []
    for i in range(size):
        x.append('-'.join(alpha[0:i] + alpha[i::-1]).center(width, '-'))
    print(*x, sep = '\n')
    print(*x[-2 :: -1], sep = '\n')

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)



