#Find the  total number of pair of socks from the given array where n = elements in the array.
def sock (a, b):
    count=0			# keeps a count of number of pairs
    i=0			# keeps a count of number of socks
    b.sort()
    b.append('#')
    while i < a:
        if b[i] == b[i+1]:
            count += 1
            i += 2		
        else:
            i += 1
    return count

x = 10
y = [1,1,3,1,2,1,3,3,3,3]
print(sock(x, y))