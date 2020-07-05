from collections import deque
N = int(input())
d = deque()
for k in range(N):
    i= input().split()   
    if i[0] == 'append':
        d.append(i[1])
    elif i[0] == 'appendleft':
        d.appendleft(i[1])
    elif i[0] == 'pop':
        d.pop()
    else:
        d.popleft()
        
print(*d)