from collections import Counter
N = int(input())
a = [int(input()) for _ in range(N)]
cnt = 0
for i in Counter(a).values():
    if i%2==1: cnt+=1
print(cnt)
