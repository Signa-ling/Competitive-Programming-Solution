# ローカル実行環境の作成
# ファイルのオープン

inp = open("./test_env/input.txt", mode="r")


# ----ここからプログラム----
from math import gcd
from itertools import combinations as com
n = int(inp.readline())
ans = 0
a = [6*(n-1) for _ in range(1,n)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i%j==0 or j%i==0:
            print(i, j)
            ans += min(i, j)
print(sum(a))

print(ans)
# ----ここまでプログラム----


# ファイルのクローズ
inp.close()
