# ローカル実行環境の作成
# ファイルのオープン

inp = open("./test_env/input.txt", mode="r")


# ----ここからプログラム----
# from collections import Counter
# import math
x = int(inp.readline())
A = [i for i in range(-118, 120)]
B = [i for i in range(-119, 119)]
for i in range(A):
    for j in range(B):
        a, b = i**5, j**5
        if a-b==x:
            print(i, j)
            exit()

# ----ここまでプログラム----

# ファイルのクローズ
inp.close()
