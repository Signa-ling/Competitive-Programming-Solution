n, m = list(map(int, input().split()))
A = sum(list(map(int, input().split())))
print(n-A if n-A>-1 else -1)
