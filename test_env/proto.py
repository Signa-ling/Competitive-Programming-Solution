# ローカル実行環境の作成
# ファイルのオープン

inp = open("./test_env/input.txt", mode="r")


# ----ここからプログラム----
n = int(inp.readline())
a = set(list(map(int, inp.readline().split())))
print('YES' if len(a)==n else 'NO')
# ----ここまでプログラム----



# ファイルのクローズ
inp.close()
