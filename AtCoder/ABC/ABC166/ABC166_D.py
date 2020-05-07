x = int(input())
for i in range(-118, 120):
    for j in range(-119, 119):
        a, b = i**5, j**5
        if a-b==x:
            print(i, j)
            exit()
