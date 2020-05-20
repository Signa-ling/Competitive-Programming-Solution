# ローカル実行環境の作成
# ファイルのオープン

inp = open("./test_env/input.txt", mode="r")


# ----ここからプログラム----

# 数数えるやつ
# from collections import Counter

from collections import deque

# 組み合わせのやつ
# from itertools import combinations as com

# 順列のやつ
# from itertools import permutations as per

# 重複有りの順列のやつ
# from itertools import product as pro

# from math import sqrt, factorial
# import numpy as np


s = deque(inp.readline().replace('\n', ''))
q = int(inp.readline())
flag = True
for i in range(q):
    query = list(map(str, inp.readline().split()))
    if query[0]=='1':
        if flag: flag = False
        else: flag = True
    else:
        # print(query[2])
        if (not flag and query[1]=='1') or flag and query[1]=='2':
            s.append(query[2])
        else:
            s.appendleft(query[2])
s = ''.join(s)
print(s if flag else s[::-1])
# ----ここまでプログラム----

# ファイルのクローズ
inp.close()
