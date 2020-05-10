n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
a, b = list(map(lambda x: x[0], ab)), list(map(lambda x: x[1], ab))
zip_ab = list(zip(sorted(a), sorted(b)))
s, g = zip_ab[n//2]
ans = [abs(i-j) + abs(s-i) + abs(g-j) for i, j in ab]
print(sum(ans))
