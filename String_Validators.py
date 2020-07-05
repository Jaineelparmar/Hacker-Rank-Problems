# Python has built-in string validation methods for basic data.
# It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

if __name__ == '__main__':
    s = input()
    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    s = list(s)
    for i in range(len(s)):
        if s[i].isalnum() == True:
            alnum = True
        if s[i].isalpha() == True:
            alpha = True
        if s[i].isdigit() == True:
            digit = True
        if s[i].islower() == True:
            lower = True
        if s[i].isupper() == True:
            upper = True
    s =''.join(s)
    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper) 
