#In this challenge, the user enters a string and a substring.
#You have to print the number of times that the substring occurs in the given string. 
#String traversal will take place from left to right, not from right to left.

def count_substring(a, b):
    z=0
    for i in range(len(a)):
        if a[i] == b:
            z += 1
            
    return z

x = input().strip().split(' ')
y = input()

print(count_substring(x, y))


#OR

def count_substring(a, b):
    z=0
    for i in a:
        if i == b:
            z += 1
            
    return z

x = input().strip()
y = input().strip()

print(count_substring(x, y))