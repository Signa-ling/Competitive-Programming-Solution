x, y, a, b, c = map(int, input().split())
r = list(map(int, input().split()))
g = list(map(int, input().split()))
cl = list(map(int, input().split()))
r.sort(reverse=True)
g.sort(reverse=True)
ans = r[:x] + g[:y] + cl
print(sum(sorted(ans, reverse=True)[:x+y]))
