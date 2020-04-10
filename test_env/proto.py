# ローカル実行環境の作成
# ファイルのオープン

inp = open("./test_env/input.txt", mode="r")


# ----ここからプログラム----
from collections import deque
n = int(inp.readline())
A = inp.readline().split()
ans = deque()
cnt = 1
for a in A:
    if cnt%2==n%2: ans.appendleft(a)
    else: ans.append(a)
    cnt+=1
print(' '.join(ans))
# ----ここまでプログラム----


# ファイルのクローズ
inp.close()
