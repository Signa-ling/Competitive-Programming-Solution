S = input()
ans = 0
for i in range(2**(len(S)-1)):
    s = ''
    for j in range(len(S)):
        s += S[j]
        if (i>>j) & 1: s+='+'
    ans+=eval(s)
print(ans)
