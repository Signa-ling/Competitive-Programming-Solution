from collections import Counter as c
n = int(input())
a = n//11
print(2*a if n%11==0 else 2*a+1 if n%11<=6 else 2*a+2)
