# ローカル実行環境の作成
# ファイルのオープン

inp = open("./test_env/input.txt", mode="r")


# ----ここからプログラム----
from collections import Counter as cnt
n = int(inp.readline())
S = [inp.readline().replace('\n', '') for _ in range(n)]
S = cnt(S)
m = max(S.values())
S = sorted(S.items(), key=lambda x: x[0])
for s, i in S:
    if i==m: print(s)

# ----ここまでプログラム----


# ファイルのクローズ
inp.close()
