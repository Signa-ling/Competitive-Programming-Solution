# ローカル実行環境の作成
# ファイルのオープン

inp = open("./test_env/input.txt", mode="r")


# ----ここからプログラム----
a, b, x = map(int, inp.readline().split())
minN, maxN = 0, x+1
while minN+1<maxN:
    tmp = (minN+maxN)//2
    if a*tmp+b*len(str(tmp))<=x: minN=tmp
    else: maxN=tmp
    print(minN, maxN)
print(min(minN, 10**9))

# ----ここまでプログラム----



# ファイルのクローズ
inp.close()
