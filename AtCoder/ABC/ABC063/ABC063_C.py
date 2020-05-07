N = int(input())
h = [int(input()) for _ in range(N)]
ans = sum(h)
if ans%10!=0:
    print(ans)
else:
    s = [i for i in h if i%10]
    print(ans - min(s) if len(s) else 0)
