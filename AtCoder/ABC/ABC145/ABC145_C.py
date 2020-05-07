from math import sqrt, factorial
from itertools import permutations as pe
N = int(input())
X = [list(map(int,input().split())) for _ in range(N)]
l = [i for i in range(N)]
d = 0
for i in pe(l):
    flag = False
    dd = 0
    x, y, xx, yy = 0, 0, 0, 0

    for ii in i:
        if flag:
            xx, yy = X[ii][0], X[ii][1]
            dd += sqrt((x-xx)**2+(y-yy)**2)
            flag=False
        x, y = X[ii][0], X[ii][1]
        flag=True
    d+=dd
print(d/factorial(N))
