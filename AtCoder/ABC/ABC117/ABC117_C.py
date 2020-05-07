n, m = map(int, input().split())
k = list(map(int, input().split()))
d = [0]*(m-1)
k.sort()
for i in range(m-1):
    d[i] = abs(k[i]-k[i+1])
d = sorted(d, reverse=True)
print(sum(d)-sum(d[:n-1]))
