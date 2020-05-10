# ローカル実行環境の作成
# ファイルのオープン

inp = open("./test_env/input.txt", mode="r")


# ----ここからプログラム----
# from collections import Counter
# from itertools import combinations as com
# from itertools import product as pro
# import math
import numpy as np

m = int(inp.readline())
mxy = [tuple(map(int, inp.readline().split())) for _ in range(m)]
smxy = set(mxy)
n = int(inp.readline())
nxy = [list(map(int, inp.readline().split())) for _ in range(n)]
nx, ny = np.array(list(map(lambda x: x[0], nxy))), np.array(list(map(lambda x: x[1], nxy)))
for i in range(m):
    x, y = mxy[i]
    for j in range(n):
        x2, y2 = nxy[j]
        xx, yy = x-x2, y-y2
        nx, ny = nx + xx, ny + yy
        ab = set([(a, b) for a, b in zip(nx, ny)])
        if len(smxy & ab) == m:
            # print(smxy)
            # print(ab)
            print(xx*-1, yy*-1)
            exit()
        nx, ny = nx - xx, ny - yy
# ----ここまでプログラム----

# ファイルのクローズ
inp.close()
