n, k = map(int, input().split())
h = list(map(int, input().split()))
h = sorted(h, reverse=True)
print(sum(h[k:]))
