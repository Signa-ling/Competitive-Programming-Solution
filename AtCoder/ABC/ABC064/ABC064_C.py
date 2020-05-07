n = int(input())
a = list(map(int,input().split()))
color = [399, 799, 1199, 1599, 1999, 2399, 2799, 3199, 4800]
num = [0]*9
for i in a:
    for j in range(9):
        if i<=color[j]:
            num[j]+=1
            break
s = [1 for i in num[:8] if i>0]
print(max(sum(s), 1), sum(s)+num[8])
