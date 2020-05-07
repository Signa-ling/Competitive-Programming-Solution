n = int(input())
a = list(map(int, input().split()))
plus, minus = 0, 0
ans = 1
for i in range(n-1):
    if a[i]<a[i+1]: plus = 1
    elif a[i]>a[i+1]: minus = 1
    if plus==minus==1:
        plus, minus = 0, 0
        ans += 1
print(ans)
