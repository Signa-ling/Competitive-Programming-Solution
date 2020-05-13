# ローカル実行環境の作成
# ファイルのオープン

inp = open("./test_env/input.txt", mode="r")


# ----ここからプログラム----
# from collections import Counter
# from itertools import combinations as com
# from itertools import product as pro
# import math
# import numpy as np

def binarySearch(n, S, t):
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if S[mid]==t: return 1
        elif t < S[mid]: right = mid
        else: left = mid + 1

    return 0


n = int(inp.readline())
S = list(map(int, inp.readline().split()))
q = int(inp.readline())
T = list(map(int, inp.readline().split()))
cnt = 0
for i in range(q):
    cnt += binarySearch(n, S, T[i])

print(cnt)

# ----ここまでプログラム----

# ファイルのクローズ
inp.close()
