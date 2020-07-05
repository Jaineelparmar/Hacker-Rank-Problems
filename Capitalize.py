
def solve(s):
    # for i in s.split():
    #     str = i.capitalize()
    #     print(str)

    str = [i.capitalize() for i in s.split() ]
    # print(*str)
    
    for i in str:
        s = s.replace(i.lower(), i)
    return s

if __name__ == '__main__':
    s = input()
    print(solve(s))
