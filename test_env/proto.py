# ローカル実行環境の作成
# ファイルのオープン

inp = open("./test_env/input.txt", mode="r")


# ----ここからプログラム----
n, m = map(int, inp.readline().split())
ac, wa = 0, 0
ac = [0]*(n+1)
wa = [0]*(n+1)
ans1, ans2 = 0, 0
for i in range(m):
    p, s = map(str, inp.readline().split())
    if ac[int(p)]==1: continue
    if s=='AC':
        ac[int(p)] = 1
        ans1 += 1
        ans2 += wa[int(p)]
    else:
        wa[int(p)] += 1

print(ans1, ans2)
# ----ここまでプログラム----



# ファイルのクローズ
inp.close()
