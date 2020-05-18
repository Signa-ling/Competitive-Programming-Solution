# ローカル実行環境の作成
# ファイルのオープン

inp = open("./test_env/input.txt", mode="r")


# ----ここからプログラム----

# 数数えるやつ
# from collections import Counter

# 組み合わせのやつ
# from itertools import combinations as com

# 順列のやつ
# from itertools import permutations as per

# 重複有りの順列のやつ
# from itertools import product as pro

# from math import sqrt, factorial
# import numpy as np


p = float(inp.readline())
pp = int(p+1)
for x in range(pp+1):
    t = (pp-x) + 2**(x/1.5)
# ----ここまでプログラム----

# ファイルのクローズ
inp.close()
