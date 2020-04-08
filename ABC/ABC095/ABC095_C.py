a,b,c,x,y = map(int,input().split())
ab = min(a+b, c*2)
if x>y:
    tmp, tmp2, tmp3 = y, (x-y)*a, (x-y)*ab
else:
    tmp, tmp2, tmp3 = x, (y-x)*b, (y-x)*ab
ans = 0
for i in range(tmp):
    ans += ab
print(ans+min(tmp2, tmp3))
