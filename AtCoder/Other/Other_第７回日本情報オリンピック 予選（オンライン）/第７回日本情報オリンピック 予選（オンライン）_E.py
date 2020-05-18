r, c = map(int, input().split())
A = [list(map(int, input().split()))for _ in range(r)]
ans = 0
for i in range(2**r):
    t = 0
    for j in range(c):
        tt = 0
        for k in range(r):
            if (i & (1 << k)) and A[k][j] == 1:
                tt += 1
            elif not (i & (1 << k)) and A[k][j] == 0:
                tt += 1
        t += max(tt, r-tt)
    ans = max(ans, t)
print(ans)
