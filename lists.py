# Consider a list (list = []). You can perform the following commands:
# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.


if __name__ == '__main__':
    N = int(input())
    list = []
    list.insert(0, 5)       # .insert(index, value)
    list.insert(1, 10)      # .insert(index, value)
    list.insert(0, 6)       # .insert(index, value)
    print(list)
    list.remove(6)          # .remove(value)
    list.append(9)          # .append(value)
    list.append(1)
    list.sort(key=None, reverse=False)
    print(list)
    list.pop()
    list.reverse()
    print(list)



# OR 


if __name__ == '__main__': 
    N = int(input()) 
    l = [] 
    for _ in range(N): 
        s = input().split() 
        if s[0] == 'insert': 
            l.insert(int(s[1]), int(s[2])) 
        elif s[0] == 'remove': 
            l.remove(int(s[1])) 
        elif s[0]== 'append':
             l.append(int(s[1])) 
        elif s[0] == 'sort': 
            l.sort() 
        elif s[0] == 'print': 
            print(l) 
        elif s[0] == 'reverse': 
            l.reverse() 
        elif s[0] == 'pop': 
            l.pop()