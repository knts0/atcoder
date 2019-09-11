import numpy as np

n = int(input())
ans = np.zeros((n, n))

for i in range(n):
    lst = list(map(int,input().split()))

    if lst[1] > 0:
        u = lst[0]
        for v in lst[2:]:
            ans[u - 1][v - 1] = 1

for i in range(n):
    for j in range(n):
        print(str(int(ans[i][j])) + " ", end="")
    print("")