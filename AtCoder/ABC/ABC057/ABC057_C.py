import math
n = int(input())
a = int(math.modf(n**0.5)[1])
aa = []
for i in range(1, a+1):
    if n%i==0:
        aa.append([len(str(i)), len(str(n//i))])
print(aa[-1][1])
