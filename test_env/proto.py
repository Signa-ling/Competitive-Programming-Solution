# ローカル実行環境の作成
# ファイルのオープン

inp = open("./test_env/input.txt", mode="r")


# ----ここからプログラム----
N = int(inp.readline())
A = [list(map(int, inp.readline().split())) for i in range(N)]
A = sorted(A, key=lambda x: x[1])

work = 0
for a in A:
    work += a[0]

    if work>a[1]:
        print('No')
        exit()

print('Yes')

# ----ここまでプログラム----

# ファイルのクローズ
inp.close()
