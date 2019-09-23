n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

dp = [[0, 0, 0] for _ in range(n + 1)]

for i in range(n):
    for j in range(3):
        dp[i + 1][j] = max(dp[i][(j + 1) % 3] + a[i][j], dp[i][(j + 2) % 3] + a[i][j])

print(max(dp[n]))