w = int(input())
n, k = map(int, input().split())
a = [0] * n
b = [0] * n
for i in range(n):
    aa, bb = map(int, input().split())
    a[i] = aa
    b[i] = bb

dp = [[[-1] * 10010 for _ in range(55)] for _ in range(55)]
dp[0][0] = 0
for i in range(n):
    for j in range(n):
        for k in range(w + 1):
            if not dp[i][j][k] == -1 and k + a[i] <= w and j + b[i] <= n:
                dp[i + 1][j + 1][k + a[i]] = dp[i][j][k] + b[i]
                dp[i + 1][j][k] = dp[i][j][k]

ans = 0
for i in range(n):
    for j in range(w + 1):
        if not dp[n][i + 1][j] == -1:
            ans = max(dp[n][i + 1], ans)

print(ans)


