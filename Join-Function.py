# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

def split_join(string):
    return "-".join(string.split(" "))

x = input("Enter a line:")
print(split_join(x))