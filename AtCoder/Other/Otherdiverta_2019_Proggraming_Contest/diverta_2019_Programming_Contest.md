# [diverta 2019 Programming Contest](https://atcoder.jp/contests/diverta2019)

# 備考

- B問題の解き方をPythonで提出するとTLEするのでPypyで提出した

# [B](https://atcoder.jp/contests/diverta2019/tasks/diverta2019_b)

- 2020/04/09 解答(自力じゃない)
- 愚直にやるなら3重ループであるがNの上限が3000であることからTLEする(O(n^3))
- 2重ループでR,G,Bの内2種類の色の個数を事前に定めておく(今回はR,G)
  - i=0~3000, j=0~3000の間でRxi, Gxjを求める
  - N-Ri-Gj<0となり、尚且N-Ri-GjがBの倍数であればBがk個あれば丁度Nになる
    - が、今回はkまで求める必要は無いのでこの時点でcnt+=1する
- cntを出力しておしまい