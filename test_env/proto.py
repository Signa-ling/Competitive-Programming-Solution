# ローカル実行環境の作成
# ファイルのオープン

inp = open("./test_env/input.txt", mode="r")


# ----ここからプログラム----
n,m = map(int, inp.readline().split())
x = [list(map(int, inp.readline().split())) for _ in range(m)]
for i in range(10**n):
    a = str(i)
    if len(a)!=n: continue
    for s,c in x:
        if a[s-1]!=str(c): break
    else:
        print(i)
        exit()
print(-1)
# ----ここまでプログラム----

# ファイルのクローズ
inp.close()
