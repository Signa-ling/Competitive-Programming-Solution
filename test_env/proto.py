# ローカル実行環境の作成
# ファイルのオープン

inp = open("./test_env/input.txt", mode="r")


# ----ここからプログラム----
x, y, a, b, c = map(int, inp.readline().split())
r = list(map(int, inp.readline().split()))
g = list(map(int, inp.readline().split()))
cl = list(map(int, inp.readline().split()))

r.sort(reverse=True)
g.sort(reverse=True)

ans = r[:x] + g[:y] + cl
print(sum(sorted(ans, reverse=True)[:x+y]))

# ----ここまでプログラム----

# ファイルのクローズ
inp.close()
