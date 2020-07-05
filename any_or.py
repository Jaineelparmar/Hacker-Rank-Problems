n, l = int(input()), list(map(int,input().split()))
print(all(i>0 for i in l) and any(((str(j))[::-1] == str(j) for j in l)))