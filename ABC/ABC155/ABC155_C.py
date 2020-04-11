from collections import Counter as cnt
n = int(input())
S = [input().replace('\n', '') for _ in range(n)]
S = cnt(S)
m = max(S.values())
S = sorted(S.items(), key=lambda x: x[0])
for s, i in S:
    if i==m: print(s)
