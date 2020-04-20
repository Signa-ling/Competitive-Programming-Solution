# ローカル実行環境の作成
# ファイルのオープン

inp = open("./test_env/input.txt", mode="r")


# ----ここからプログラム----
# from collections import Counter
# import math
n = int(inp.readline())
A = list(map(int,inp.readline().split()))
B = [0]*3
for i in A:
    if i%4==0: B[0]+=1
    elif i%2==0: B[1]+=1
    else: B[2]+=1

print('Yes' if B[0]==0 and B[2]==0 or B[0]>=B[2] or B[1]==0 and B[2]-B[0]==1 else 'No')
# ----ここまでプログラム----

# ファイルのクローズ
inp.close()
