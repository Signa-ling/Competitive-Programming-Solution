n = int(input())
A = list(map(int, input().split()))
cnt = 0
B = []
for i in range(n):
    tmp = A[i]
    if tmp<0:
        tmp*=-1
        cnt+=1
    
    B.append(tmp)
print(sum(B)-min(B)*2 if cnt%2!=0 else sum(B))
