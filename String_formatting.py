def print_formatted(number):
    w = len(str(bin(number)).replace('0b',''))
    for i in range(1, n+1):
        print("{} {} {} {}".format(str(i).rjust(w), oct(i).replace('0o','').rjust(w), hex(i).replace('0x','').upper().rjust(w), bin(i).replace('0b','').rjust(w)))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)