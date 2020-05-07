n = int(input())
p = list(map(int, input().split()))
flag = 0
cnt = 0
for i in range(n):
    if flag: flag=0
    elif p[i]==i+1:
        flag=1
        cnt+=1
print(cnt)
