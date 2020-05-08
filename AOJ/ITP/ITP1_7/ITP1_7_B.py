from itertools import combinations as com
while True:
    cnt = 0
    n, x = map(int, input().split())
    if n==0 and x==0: break
    num = [i for i in range(1, n+1)]
    for i,j,k in com(num, 3):
        if i+j+k==x: cnt+=1
    print(cnt)
