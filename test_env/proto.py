# ローカル実行環境の作成
# ファイルのオープン

inp = open("./test_env/input.txt", mode="r")


# ----ここからプログラム----
# from collections import Counter
# from itertools import combinations as com
# from itertools import product as pro
# import math
# import numpy as np

S = inp.readline()
ans = 0
for i in range(2**(len(S)-1)):
    s = ''
    for j in range(len(S)):
        s += S[j]
        if i & (1 >> j): s+='+'
    ans+=eval(s)
print(ans)


# ----ここまでプログラム----

# ファイルのクローズ
inp.close()
