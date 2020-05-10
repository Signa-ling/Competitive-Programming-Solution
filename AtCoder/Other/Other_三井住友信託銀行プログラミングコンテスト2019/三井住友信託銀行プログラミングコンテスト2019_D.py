from itertools import product as pro
N = int(input())
S = input()
cnt = 0
for i, j, k in pro("0123456789", repeat=3):
    try:
        x = S.index(i)
        y = S.index(j, x + 1)
        z = S.index(k, y + 1)
    except:
        continue
    cnt += 1
print(cnt)
