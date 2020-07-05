from collections import Counter 

n, m = list(map(int, input().split())) 
array = list(map(int, input().split()))
A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))

counts = Counter(array) 
array = list(set(array)) 

happiness = 0

for each in array:
    if each in A:
        happiness += counts[each] 
    elif each in B:
        happiness -= counts[each]

print(happiness)
