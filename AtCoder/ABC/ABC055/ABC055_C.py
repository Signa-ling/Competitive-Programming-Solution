n, m = map(int, input().split())
mm = m//2
print(mm if n>mm else (mm-n)//2+n)
