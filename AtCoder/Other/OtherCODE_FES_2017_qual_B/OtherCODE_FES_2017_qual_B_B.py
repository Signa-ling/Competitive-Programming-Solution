from collections import Counter as c
n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))
flag = True
d_c = c(d)
t_c = c(t)
if n<m: flag = False
else: 
    for i,j in t_c.items():
        if d_c[i] < j:
            flag = False
            break
print('YES' if flag else 'NO')
