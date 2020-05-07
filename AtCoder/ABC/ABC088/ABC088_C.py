import numpy as np
a=[list(map(int, input().split())) for _ in range(3)]
a = np.array(a)
for i in range(3):
    a[i]-=min(a[i])
print(set(a))
print('Yes' if all(a[0]==a[1]) and all(a[1]==a[2]) else 'No')
