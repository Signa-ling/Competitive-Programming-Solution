n,m = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(m)]
for i in range(10**n):
    a = str(i)
    if len(a)!=n: continue
    for s,c in x:
        if a[s-1]!=str(c): break
    else:
        print(i)
        exit()
print(-1)
