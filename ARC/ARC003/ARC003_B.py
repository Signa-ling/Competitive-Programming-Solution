n = int(input())
S = [input()[::-1] for _ in range(n)]
S.sort()
for sr in S:
    print(sr[::-1])
