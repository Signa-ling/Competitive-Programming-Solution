s=input().replace('\n', '')
t=input().replace('\n', '')
begin, end = len(s) - len(t), len(s)
ans=''
while begin>=0:
    origin = s[begin:end]
    flag=1
    for i in range(len(t)):
        if origin[i]!=t[i] and origin[i]!='?':
            flag=0
            break
    if flag:
        ans = s[:begin]+t+s[end:]
        break
    begin-=1
    end-=1
print("UNRESTORABLE" if not len(ans) else ans.replace('?', 'a'))
