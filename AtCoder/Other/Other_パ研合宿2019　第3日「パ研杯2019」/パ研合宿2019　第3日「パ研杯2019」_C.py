n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(m-1):
    for j in range(1, m):
        pt = 0
        for k in range(n):
            pt += max(a[k][i], a[k][j])
        ans = max(ans, pt)
print(ans)
