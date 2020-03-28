X = int(input())
a = X
ans = 0
while a >= 5:
    if a > 499:
        a -= 500
        ans+=1000
    else:
        a-=5
        ans+=5
print(ans)
