# Find the longest even word from the given string.

def lew(a):

    words =[i for i in a.split() if len(i)%2 == 0]

    if len(words) == 0:
        return False
    else:
        max_len = words[0]
        for i in words:
            if len(i) > len(max_len):
                max_len = i
                
    return max_len

print(lew("It is a pleasant day today"))



# Find the longest odd word from the given string.

def low(a):

    words =[i for i in a.split() if len(i)%2 != 0]

    if len(words) == 0:
        return False
    else:
        max_len = words[0]
        for i in words:
            if len(i) > len(max_len):
                max_len = i
                
    return max_len

print(low("It is a pleasant day today"))