# ローカル実行環境の作成
# ファイルのオープン

inp = open("./test_env/input.txt", mode="r")


# ----ここからプログラム----
# from collections import Counter
# import math
n = int(inp.readline())
A = list(map(int, inp.readline().split()))
ans = 10**9
x, y = 0, sum(A)
for i in range(n-1):
    x += A[i]
    y -= A[i]
    ans = min(ans, abs(x-y))
print(ans)

# ----ここまでプログラム----

# ファイルのクローズ
inp.close()
