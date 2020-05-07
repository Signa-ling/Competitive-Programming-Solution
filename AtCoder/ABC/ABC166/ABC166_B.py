n, k = map(int, input().split())
N = [0]*(n)
for i in range(k):
    d = int(input())
    A = list(map(int, input().split()))
    for j in A:
        if N[j-1]==0: N[j-1] = 1
print(n-sum(N))
