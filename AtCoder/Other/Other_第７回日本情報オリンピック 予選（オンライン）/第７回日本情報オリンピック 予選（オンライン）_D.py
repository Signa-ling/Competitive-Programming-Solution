import numpy as np
m = int(input())
mxy = [tuple(map(int, input().split())) for _ in range(m)]
smxy = set(mxy)
n = int(input())
nxy = [list(map(int, input().split())) for _ in range(n)]
nx, ny = np.array(list(map(lambda x: x[0], nxy))), np.array(list(map(lambda x: x[1], nxy)))
for i in range(m):
    x, y = mxy[i]
    for j in range(n):
        x2, y2 = nxy[j]
        xx, yy = x-x2, y-y2
        nx, ny = nx + xx, ny + yy
        ab = set([(a, b) for a, b in zip(nx, ny)])
        if len(smxy & ab) == m:
            
            
            print(xx*-1, yy*-1)
            exit()
        nx, ny = nx - xx, ny - yy
