n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
a, b = list(map(lambda x: x[0], ab)), list(map(lambda x: x[1], ab))
zip_ab = list(zip(sorted(a), sorted(b)))
s, g = zip_ab[n//2]
ans = 0
for i,j in ab:
    if s<=i and j<=g: ans+=g-s
    elif i<s and j<=g: ans += (s-i)*2 + g-s
    elif s<=i and g<j: ans += g-s + (j-g)*2
    else: ans += (s-i)*2 + (j-g)*2 + g-s
print(ans)
