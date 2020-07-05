n = int(input())
for i in range(n):
    N = int(input())
    Na = set(map(int, input().split()))
    M = int(input())
    Ma = set(map(int, input().split()))
    print(Na.issubset(Ma))