n,x=input().split()
l = []
for i in range(int(x)):
    l.append(input().split()) 
for i in zip(*l):
    i=list(map(float,i))
    print(round(sum(i)/int(x),1)) 

#OR

n,x=input().split()
l=[input().split() for i in range(int(x))]
for i in zip(*l):
    i=list(map(float,i))
    print(round(sum(i)/int(x),1)) 