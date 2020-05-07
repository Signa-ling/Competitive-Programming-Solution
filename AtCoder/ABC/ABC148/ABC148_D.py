from collections import deque
n = int(input())
r = deque(map(int, input().split()))
i=0
while True:
    if max(len(r),i)==i:
        break
    if r[i]!=i+1:
        r.popleft()
    else:
        i+=1
print('-1' if len(r)==0 else n-len(r))
