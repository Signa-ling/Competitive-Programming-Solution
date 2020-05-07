n = int(input())
cnt = 0
ans = 0
while(n>1):
    n=n//2
    cnt+=1
# print(cnt)
for i in range(cnt+1):
    ans+=2**i
print(ans)
