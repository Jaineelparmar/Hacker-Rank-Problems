from itertools import groupby
S = input()
for k, g in groupby(S):
    # print(g, int(k))
    # print(list(g), int(k))
    x = len(list(g)), int(k)
    print(tuple(x), end='')


#OR

# from itertools import groupby
# S = input()
# x = [(len(list(g)), int(k)) for k, g in groupby(S)]
# print(*x)

#OR

# from itertools import groupby
# x = [(len(list(g)), int(k)) for k, g in groupby(input())]
# print(*x)

#OR

# from itertools import groupby
# print(*[(len(list(c)), int(k)) for k, c in groupby(input())])

