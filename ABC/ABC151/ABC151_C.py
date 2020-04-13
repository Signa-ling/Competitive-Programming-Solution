n, m = map(int, input().split())
ac = [0]*(n+1)
wa = [0]*(n+1)
ans1, ans2 = 0, 0
for i in range(m):
    p, s = map(str, input().split())
    if ac[int(p)]==1: continue
    if s=='AC':
        ac[int(p)] = 1
        ans1 += 1
        ans2 += wa[int(p)]
    else:
        wa[int(p)] += 1
print(ans1, ans2)
