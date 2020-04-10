S = input()
a = ['maerd', 'remaerd', 'esare', 'resare']
tmp =''
for s in S[::-1]:
    tmp += s
    if tmp in a: tmp=''
print('YES' if len(tmp)==0 else'NO')
