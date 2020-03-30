# ローカル実行環境の作成
# ファイルのオープン

inp = open("./test_env/input.txt", mode="r")


# ----ここからプログラム----
n = int(inp.readline())
S = [inp.readline().replace('\n', '')[::-1] for _ in range(n)]
S.sort()
for sr in S:
    print(sr[::-1])
# ----ここまでプログラム----

# ファイルのクローズ
inp.close()
