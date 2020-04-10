from collections import deque
n = int(input())
A = input().split()
ans = deque()
cnt = 1
for a in A:
    if cnt%2==n%2: ans.appendleft(a)
    else: ans.append(a)
    cnt+=1
print(' '.join(ans))
