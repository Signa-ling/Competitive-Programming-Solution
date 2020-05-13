def binarySearch(n, S, t):
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if S[mid]==t: return 1
        elif t < S[mid]: right = mid
        else: left = mid + 1
    return 0
n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))
cnt = 0
for i in range(q):
    cnt += binarySearch(n, S, T[i])
print(cnt)
