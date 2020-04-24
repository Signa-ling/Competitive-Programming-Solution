# ローカル実行環境の作成
# ファイルのオープン

inp = open("./test_env/input.txt", mode="r")


# ----ここからプログラム----
# from collections import Counter
# import math
A = list(map(int, inp.readline().split()))
m3, suma = max(A)*3, sum(A)
print((m3-suma)//2 if (m3-suma)%2==0 else (m3-suma)//2 + 2)
# ----ここまでプログラム----

# ファイルのクローズ
inp.close()
