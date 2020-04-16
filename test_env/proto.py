# ローカル実行環境の作成
# ファイルのオープン

inp = open("./test_env/input.txt", mode="r")


# ----ここからプログラム----
C = inp.readline()
ans = ''
flag=True
for c in C:
    if c==' ' and flag:
        c = ','
        flag=False
    elif c!=' ':
        flag=True
    ans+=c
print(ans)

# ----ここまでプログラム----



# ファイルのクローズ
inp.close()
