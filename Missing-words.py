## Find the missing words from the given two strings

# Code 1:

x="I am using HackerRank to improve programming"
y="am HackerRank to improve"

a=x.split(' ')
print(a)

b=y.split(' ')
print(b)

s1=set(a)
s2=set(b)

# difference = Return the difference of two or more sets as a new set. (i.e. all elements that are in this set but not the others.)
print(list(s1.difference(s2)))


# Code 2:

x="I am using HackerRank to improve programming"
y="am HackerRank to improve"
li=[]

for word in x.split():
    if word not in y.split():
        li.append(word)
        
print(li)