n, k = map(int, input().split())
A = list(map(int, input().split()))
B = [(1+i)/2 for i in A]
ans = sum(B[:k])
t = ans
for i in range(n-k):
    t-=B[i]
    t+=B[i+k]
    if t>ans: ans=t
print(ans)
