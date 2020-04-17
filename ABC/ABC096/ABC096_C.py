h, w = map(int,input().split())
a = []
flag = True
for i in range(h):
    aa = list(input().rstrip())
    a.append(aa)
for i in range(h):
    for j in range(w):
        if a[i][j]=='.': continue
        aa = ['','','','']
        if i!=0: aa[0] = a[i-1][j]
        if i+1!=h: aa[1] = a[i+1][j]
        if j!=0: aa[2] = a[i][j-1]
        if j+1!=w: aa[3] = a[i][j+1]
        if a[i][j] not  in aa:
            flag = False
            break
print('Yes' if flag else 'No')
