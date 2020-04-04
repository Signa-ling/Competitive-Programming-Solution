N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
A = sorted(A, key=lambda x: x[1])
work = 0
for a in A:
    work += a[0]
    if work>a[1]:
        print('No')
        exit()
print('Yes')
