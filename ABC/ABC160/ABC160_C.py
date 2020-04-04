N, K = map(int, input().split())
a = list(map(int, input().split()))
dist = []
for i in range(K):
    if i == K-1:
        d = a[0] - 0 + N - a[i]
    else:
        d = a[i+1] - a[i]
    dist.append(d)
dist.sort()
dist.pop(-1)
print(sum(dist))
