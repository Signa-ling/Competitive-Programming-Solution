from itertools import combinations as com
n = int(input())
abc = ['a', 'b', 'c']*n
ans = list(set([s for s in com(abc, n)]))
ans.sort()
for w in ans:
    print(''.join(w))
