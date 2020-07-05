#You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
    l = list(s)
    for i in range(0, len(l)):
        if l[i].isupper():
            l[i] = l[i].lower()
        else:
            l[i] = l[i].upper()
    return "".join(l)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)