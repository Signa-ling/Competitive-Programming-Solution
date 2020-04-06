# ローカル実行環境の作成
# ファイルのオープン

inp = open("./test_env/input.txt", mode="r")


# ----ここからプログラム----
from collections import Counter
N = int(inp.readline())
a = [int(inp.readline()) for _ in range(N)]
cnt = 0
for i in Counter(a).values():
    if i%2==1: cnt+=1
print(cnt)
# ----ここまでプログラム----

# ファイルのクローズ
inp.close()
