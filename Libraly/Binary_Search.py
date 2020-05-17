'''
二分探索

・基本的考え
 ・ソート済み配列Sを対象とする
 ・初めに配列全体を探索範囲とし以下を繰り返す
   1. 探索範囲の中央の要素S[mid]を調べる
   2. S[mid]が探している要素tであれば探索終了
   3. そうでない場合、tの大きさがS[mid]より大きいか小さいかを判別
   4. 小さければ探索範囲の右側をmidにする
   5. 大きければ探索範囲の左側をmid+1にする
   6. 4., 5.のいずれかの結果によって探索範囲を更新し1.に戻る
   7. 探索範囲の左側が右側より大きくなったら探索を打ち切る

なおpythonにはbisectと呼ばれる二分探索モジュールが存在する

'''

def binary_search(S, t):
    # 探索範囲の初期設定(全体を範囲とする)
    left, right = 0, len(S)

    # leftの値がrightより大きくなるまで繰り返す
    while left < right:

        # 探索範囲の中央値を得る
        mid = (left + right) // 2

        # 探索範囲の中央の要素が探している値tであればindexを返す
        # 中央要素よりtが小さければ探索範囲の右側をmidに置き換える
        # 中央要素よりtが大きければ探索範囲の左側をmid+1に置き換える
        if S[mid] == t: return mid
        elif t < S[mid]: right = mid
        else: left = mid + 1

    # 要素が見つからなければ-1を返す
    return -1


S = [i for i in range(100)]
t = int(input())
print(binary_search(S, t))
