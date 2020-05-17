import bisect
n = int(input())
A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))
C = sorted(list(map(int, input().split())))
cnt = 0
for i in range(n):
    a = bisect.bisect_left(A, B[i])
    c = bisect.bisect_right(C, B[i])
    cnt += a * (n-c)
print(cnt)
