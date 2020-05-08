n = int(input())
nn = [i for i in range(1, n+1) if i%2==1]
ans = 0
for i in range(1, n+1, 2):
    cnt = []
    t = 0
    for j in nn[:-2]:
        for k in nn[1:]:
            if j*k==i: cnt.extend([j, k])
    if len(set(cnt))==8:
        ans+=1
        
print(ans)
