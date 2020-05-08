# [CODE FESTIVAL 2017 qual B](https://atcoder.jp/contests/code-festival-2017-qualb)

## 備考

- 特になし

## [B](https://atcoder.jp/contests/code-festival-2017-qualb/tasks/code_festival_2017_qualb_b)

- 2020/04/08 解答
- N, M毎に各問題の点数の出現回数をカウントしておく
- M問内のj点問題の個数DjとN問内のj点問題の個数Tjを調べてDj > Tjが出現すればその時点で'NO'になる
- 全て調べ上げてDj <= Tjとなる場合は'YES'になる
- またN < Mの時点で'NO'になる(問題数Nが必要数Mに足りていないため)
