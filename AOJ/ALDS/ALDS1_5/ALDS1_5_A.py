n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
l = []
for i in range(2**n):
    s = 0
    for j in range(n):
        if i & (1<<j):
            s+=A[j]
    l.append(s)

for b in B:
    print('yes' if b in l else 'no')
