from collections import Counter as C
N = int(input())
A = list(map(int,input().split()))
c = C(A)
s = 0
for i in c.values():
    s += i*(i-1)//2
for j in A:
    print(s-(c[j]-1))
