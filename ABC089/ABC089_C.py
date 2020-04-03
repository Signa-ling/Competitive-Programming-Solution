from itertools import combinations as c
n = int(input())
S = [input().replace("\n", "")[0] for _ in range(n)]
cnt = [S.count(i) for i in "MARCH"]
print(sum(i*j*k for i, j, k in c(cnt, 3)))
