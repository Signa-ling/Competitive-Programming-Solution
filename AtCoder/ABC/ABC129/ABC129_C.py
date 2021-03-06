# 入力
n, m = map(int, input().split())

# 壊れた段の所だけTrueとしたいので1を入れる
broken = [0]*(n+1)
for i in range(m):
  broken[int(input())] = 1

# dp用の配列(段数), 余りを求めるための数字用意
# 各段から最上段へ向かう方法が何通りあるかを計算する
# すなわちdp[n](nは最上段)は既に到着しているため1が入る
dp = [0]*(n+2)
mod = int(1e9+7)
dp[n] = 1

# i段目からn段目まで向かう手法を求める
# i段目での動作はi+1段目に登る、i+2段目に登るの2通りが可能である
# → dp[i]段目はdp[i+1]とdp[i+2]の合計分だけ登る為の手法が増える事になる
for i in range(n-1, -1 , -1):

  # もしi段目がbroken[i]である → i段目が壊れている場合、dp[i]段目は動作の選択肢が無い → 0を入れる
  if broken[i]:
    dp[i] = 0

  # 割った余りを計算する
  else:
    dp[i] = (dp[i+1] + dp[i+2]) % mod

# 求めたいのは初期位置 = dp[0]から最上段へ登る為の手順数
# よって出力はdp[0]
print(dp[0])
