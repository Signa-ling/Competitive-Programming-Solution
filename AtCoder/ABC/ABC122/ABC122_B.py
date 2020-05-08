S = input()
ans = 0
acgt = ['A', 'C', 'G', 'T']
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        s = S[i:j]
        tmp = 0
        for ss in s:
            if ss not in acgt: break
            tmp += 1
        ans = max(ans, tmp)
print(ans)
