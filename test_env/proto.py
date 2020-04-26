# ローカル実行環境の作成
# ファイルのオープン

inp = open("./test_env/input.txt", mode="r")


# ----ここからプログラム----
# from collections import Counter
# import math

def cal(S):
    tmp, a, cnt = S[0], 1, 0
    flag = True
    for s in S[1:]:
        if S[0]!=s: flag=False
        if flag: a+=1
        if tmp[-1]==s:
            s = '*'
            ans += 1
        tmp += s

    return a, cnt

S = inp.readline().replace('\n', '')
k = int(inp.readline())
ans = 0
if len(list(set(S)))==1:
    ans = len(S)*k//2
else:
    a, cnt = cal(S)
    b, _ = cal(S[::-1])
    ans = cnt*k
    if S[0]==S[-1]:
        ans -= ((a//2)+(b//2)-((a+b)//2))*(k-1)
print(ans)
# ----ここまでプログラム----

# ファイルのクローズ
inp.close()
