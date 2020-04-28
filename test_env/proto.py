# ローカル実行環境の作成
# ファイルのオープン

inp = open("./test_env/input.txt", mode="r")


# ----ここからプログラム----
# from collections import Counter
# import math
n = int(inp.readline())
A = list(map(int, inp.readline().split()))
#minnum = 0
cnt = 0
B = []
for i in range(n):
    tmp = A[i]
    if tmp<0:
        tmp*=-1
        cnt+=1
    #print(tmp)
    B.append(tmp)
#print(cnt, sum(B), min(B))
print(sum(B)-min(B)*2 if cnt%2!=0 else sum(B))
# ----ここまでプログラム----

# ファイルのクローズ
inp.close()
