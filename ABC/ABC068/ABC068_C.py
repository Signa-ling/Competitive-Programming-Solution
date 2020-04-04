n, m = map(int, input().split())
ab = set()
bn = set()
for i in range(m):
    a, b = map(int, input().split())
    if a==1: ab.add(b)
    if b==n: bn.add(a)
print('POSSIBLE' if bn&ab else 'IMPOSSIBLE')
