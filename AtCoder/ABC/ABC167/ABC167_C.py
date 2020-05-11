n, m, x = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
C, A = list(map(lambda x: x[0], A)), list(map(lambda x: x[1:], A))
ans = 10**18
for i in range(2**n):
    M = [0]*m
    cost = 0
    for j in range(n):
        if (i>>j)&1:
            cost += C[j]
            for k in range(m):
                M[k] += A[j][k]
    if all([mm >= x for mm in M]): ans = min(ans, cost)
print(ans if ans!=10**18 else '-1')
