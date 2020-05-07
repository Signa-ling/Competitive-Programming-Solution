n = int(input())
l = list(map(int, input().split()))
l = sorted(l, reverse=True)
ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        cnt=1
        
        while True:
            k=j+cnt
            if n<=k or l[i]>=l[j]+l[k] or l[j]>=l[i]+l[k] or l[k]>=l[i]+l[j]:
                cnt-=1
                
                break
            
            cnt+=1
        ans+=cnt
print(ans)
