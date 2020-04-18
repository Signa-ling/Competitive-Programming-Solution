# ローカル実行環境の作成
# ファイルのオープン

inp = open("./test_env/input.txt", mode="r")


# ----ここからプログラム----
n, k = map(int, inp.readline().split())
h = list(map(int, inp.readline().split()))
h = sorted(h, reverse=True)
# print(h)
print(sum(h[k:]))
# ----ここまでプログラム----

# ファイルのクローズ
inp.close()
