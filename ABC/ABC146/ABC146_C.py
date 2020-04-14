a, b, x = map(int, input().split())
minN, maxN = 0, x+1
while minN+1<maxN:
    tmp = (minN+maxN)//2
    if a*tmp+b*len(str(tmp))<=x: minN=tmp
    else: maxN=tmp
print(min(minN, 10**9))
