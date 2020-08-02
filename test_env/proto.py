# ローカル実行環境の作成
# ファイルのオープン

inp = open("./test_env/input.txt", mode="r")


# ----ここからプログラム----

# 数数えるやつ
# from collections import Counter

# from collections import deque

# 組み合わせのやつ
# from itertools import combinations as com

# 順列のやつ
# from itertools import permutations as per

# 重複有りの順列のやつ
# from itertools import product as pro

# from math import sqrt, factorial
# import numpy as np

a, b = map(float, inp.readline().split())

print(int(a*(b*100)/100))


# ----ここまでプログラム----

# ファイルのクローズ
inp.close()
