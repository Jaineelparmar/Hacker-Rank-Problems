#The first line contains an integer N, the total number of country stamps.
#The next N lines contains the name of the country where the stamp is from.
#Find the total number of distinct country stamps.


a = int(input())

li = []
for b in range(a):
    c = input()
    li.append(c)
    
lst = []
for i in li:
    if i not in lst:
        lst.append(i)
        
print(len(lst))