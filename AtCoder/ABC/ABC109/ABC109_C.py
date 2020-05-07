def gcd(a, b):
    if b==0: return a
    else: return gcd(b, a%b)
n, x = map(int, input().split())
L = list(map(int, input().split()))
d = 0
for l in L:
    d = gcd(d, abs(x-l))
print(d)
