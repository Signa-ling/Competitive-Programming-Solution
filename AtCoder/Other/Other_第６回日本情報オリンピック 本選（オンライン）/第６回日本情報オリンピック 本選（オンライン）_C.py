n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]
sxy = set(xy)
ans = 0
for i in range(n-1):
    x1, y1 = xy[i]
    for j in range(1, n):
        x2, y2 = xy[j]
        vec_x, vec_y = x2-x1, y2-y1
        if (x1-vec_y, y1+vec_x) in sxy and (x2-vec_y, y2+vec_x) in sxy:
            ans = max(ans, vec_x**2+vec_y**2)
print(ans)
