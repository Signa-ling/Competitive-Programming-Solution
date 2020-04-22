# ローカル実行環境の作成
# ファイルのオープン

inp = open("./test_env/input.txt", mode="r")


# ----ここからプログラム----
# from collections import Counter
# import math
n, k = map(int, inp.readline().split())
A = list(map(int, inp.readline().split()))
B = [(1+i)/2 for i in A]
ans = sum(B[:k])
t = ans
for i in range(n-k):
    t-=B[i]
    t+=B[i+k]
    if t>ans: ans=t
print(ans)



# ----ここまでプログラム----

# ファイルのクローズ
inp.close()
