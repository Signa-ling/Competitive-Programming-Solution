n, m = map(int, input().split())
A = [list(map(lambda x: int(x)-1, input().split()))[1:] for _ in range(m)]
p = list(map(int, input().split()))
ans = 0
for i in range(1<<n):
    for j in range(m):
        cnt = 0
        for k in range(n):
            if ((i>>k) & 1) and k in A[j]: cnt += 1
        if cnt%2!=p[j]: break
    else: ans += 1
print(ans)
