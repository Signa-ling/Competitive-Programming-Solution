# ローカル実行環境の作成
# ファイルのオープン

inp = open("./test_env/input.txt", mode="r")


# ----ここからプログラム----
from itertools import combinations as c
n = int(inp.readline())
S = [inp.readline().replace("\n", "")[0] for _ in range(n)]
cnt = [S.count(i) for i in "MARCH"]
print(sum(i*j*k for i, j, k in c(cnt, 3)))

# ----ここまでプログラム----

# ファイルのクローズ
inp.close()
