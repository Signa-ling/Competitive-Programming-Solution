N = int(input())
a = list(map(int, input().split()))
a_dict = {j: i+1 for i, j in enumerate(a)}
for k, v in sorted(a_dict.items(), reverse=True):
    print(v)
