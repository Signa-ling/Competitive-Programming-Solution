n = int(input())
a = list(map(int,input().split()))
cnt = [0] * (10**5+2)
for i in a:
    cnt[i]+=1
    cnt[i+1]+=1
    cnt[i-1]+=1
print(max(cnt))
