a,b,c,d = [int(input()) for _ in range(4)] #LIST COMPREHENSION
print(pow(a, b) + pow(c, d))

#OR

a,b,c,d = (int(input()) for _ in range(4)) 
print(pow(a, b) + pow(c, d))

#OR

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(pow(a, b) + pow(c, d))
