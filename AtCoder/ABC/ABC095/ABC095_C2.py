a, b, c, x, y = map(int, input().split())
ab = c*2
if a+b > ab:
    t = ab*min(x,y)
    d = max(x,y)-min(x,y)
    if x>y: dd = a*d
    else: dd = b*d
    print(t+ab*d if dd>ab*d else t+dd)
else:
    print(a*x+b*y)
