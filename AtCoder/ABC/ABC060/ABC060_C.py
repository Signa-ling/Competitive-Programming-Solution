n, T = map(int, input().split())
t = list(map(int,input().split()))
t.append(t[-1]+T)
x = 0
for i in range(n):
    x += min(T, t[i+1] - t[i])
print(x)
