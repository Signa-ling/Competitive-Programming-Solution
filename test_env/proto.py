# ローカル実行環境の作成
# ファイルのオープン

inp = open("./test_env/input.txt", mode="r")


# ----ここからプログラム----
N = int(inp.readline())
h = list(map(int, inp.readline().split()))
cnt = 0
while True:
    if max(h) == 0:
        print(cnt)
        break
    i = 0
    while i < N:
        if h[i] == 0:
            i += 1
        else:
            cnt += 1
            while i < N and h[i] > 0:
                h[i] -= 1
                i += 1



# ----ここまでプログラム----

# ファイルのクローズ
inp.close()
