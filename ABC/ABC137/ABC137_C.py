# 入力情報の格納
n = int(input())

# 文字列をソートしてリストへ
strs = ["".join(sorted(list(input()))) for _ in range(n)]

# その他必要なもの
ans = {}
cnt = 0

for i in range(n):
  # 格納済みであれば対応した文字列のvalを加算
  # 未格納の文字列であれば{strs[i]: val}の形で辞書に追加, valの初期値は1
  if strs[i] in ans:
    cnt += ans[strs[i]]
    ans[strs[i]] +=  1
  else:
    ans[strs[i]] = 1

# cntを出力してend
print(cnt)