from itertools import permutations as pe
N = int(input())
P = tuple(map(int,input().split()))
Q = tuple(map(int,input().split()))
l = [i for i in range(1, N+1)]
p, q = 0, 0
for i,j  in enumerate(pe(l)):
    if j==P:
        p = i+1
    if j==Q:
        q = i+1
print(abs(p-q))
