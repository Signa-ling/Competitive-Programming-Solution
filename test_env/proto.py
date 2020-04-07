# ローカル実行環境の作成
# ファイルのオープン

inp = open("./test_env/input.txt", mode="r")


# ----ここからプログラム----
from collections import Counter as C

N = int(inp.readline())
A = list(map(int,inp.readline().split()))
c = C(A)
s = 0
for i in c.values():
    s += i*(i-1)//2
for j in A:
    print(s-(c[j]-1))


# ----ここまでプログラム----

# ファイルのクローズ
inp.close()
