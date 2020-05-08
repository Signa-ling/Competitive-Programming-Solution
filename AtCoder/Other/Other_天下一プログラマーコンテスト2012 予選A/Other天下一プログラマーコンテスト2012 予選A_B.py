C = input()
ans = ''
flag=True
for c in C:
    if c==' ' and flag:
        c = ','
        flag=False
    elif c==' ' and not flag:
        continue
    else:
        flag=True
    ans+=c
print(ans)
