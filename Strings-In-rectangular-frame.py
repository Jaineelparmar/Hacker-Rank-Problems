
# Write a function that takes a list of strings an prints them, one per line, in a rectangular frame. For example the list ["Hello", "World", "in", "a", "frame"] gets printed as:
#  *********
#  * Hello *
#  * World *
#  * in    *
#  * a     *
#  * frame *
#  *********
print('*'*9+'\n'+'* '+'Hello'+' *'+'\n'+'* '+'World'+' *'+'\n'+'* '+'in   '+' *'+'\n'+'* '+'a    '+' *'+'\n'+'* '+'frame'+' *'+'\n'+'*'*9)


#In Python source code, an f-string is a formatted string literals, prefixed with 'f', which contains expressions inside braces.
#The expressions are replaced with their values. The key point here is that an f-string is really an expression evaluated at run time, not a constant value.

#or for as per lengths
p=input("words?")
def frame(words):
    size = len(max(words, key=len))
    print('*' * (size + 4))
    for word in words:
        print(f'* {word} *')
    print('*' * (size + 4))
frame(p.split(" "))


#or for different lengths
p=input("words?")
def frame(words):
    size = len(max(words, key=len))
    print('*' * (size + 4))
    for word in words:
        print('* {a:<{b}} *'.format(a=word, b=size))
    print('*' * (size + 4))
frame(p.split(" "))


