from collections import deque
s = deque(input().replace('\n', ''))
q = int(input())
flag = True
for i in range(q):
    query = list(map(str, input().split()))
    if query[0]=='1':
        if flag: flag = False
        else: flag = True
    else:
        
        if (not flag and query[1]=='1') or flag and query[1]=='2':
            s.append(query[2])
        else:
            s.appendleft(query[2])

s = list(s)
if not flag:
    s = s[::-1]

print(''.join(s))
