n, k = map(int, input().split())
r, s, p = map(int, input().split())
S = list(input())
ans = 0
rsp = ['']*n
for i, op in enumerate(S):
    if op=='r': me, pt = 'p', p
    elif op=='s': me, pt = 'r', r
    else: me, pt = 's', s
    if i-k>=0 and rsp[i-k]==me: me, pt = '', 0
    ans+=pt
    rsp[i] = me
print(ans)