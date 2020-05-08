# ローカル実行環境の作成
# ファイルのオープン

inp = open("./test_env/input.txt", mode="r")


# ----ここからプログラム----
# from collections import Counter
# from itertools import combinations as com
# import math
n, m = map(int, inp.readline().split())
a = [list(map(int, inp.readline().split())) for _ in range(n)]
ans = 0
for i in range(m-1):
    for j in range(1, m):
        pt = 0
        for k in range(n):
            pt += max(a[k][i], a[k][j])
        ans = max(ans, pt)
print(ans)
# ----ここまでプログラム----

# ファイルのクローズ
inp.close()
