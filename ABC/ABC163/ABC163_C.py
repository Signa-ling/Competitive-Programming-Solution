from collections import Counter
n = int(input())
A = list(map(int, input().split()))
ca = Counter(A)
for i in range(1, n+1):
    print(ca[i])
