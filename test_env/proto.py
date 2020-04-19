# ローカル実行環境の作成
# ファイルのオープン

inp = open("./test_env/input.txt", mode="r")


# ----ここからプログラム----
# from collections import Counter
import math
n = int(inp.readline())
print(2*n*math.pi)
# ----ここまでプログラム----

# ファイルのクローズ
inp.close()
