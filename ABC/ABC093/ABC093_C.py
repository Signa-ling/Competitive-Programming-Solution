A = list(map(int, input().split()))
m3, suma = max(A)*3, sum(A)
print((m3-suma)//2 if (m3-suma)%2==0 else (m3-suma)//2 + 2)
