n, m = map(int, input().split())
A = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(m)]
ans = 0
for i in range(2**n):
    l = []
    for j in range(n):
        if (1<<j) & i: l.append(j)

    flag = True
    for x in range(len(l)-1):
        for y in range(x+1, len(l)):
            if (l[x], l[y]) not in A:
                flag = False
                break
    if flag: ans = max(ans, len(l))
print(ans)
