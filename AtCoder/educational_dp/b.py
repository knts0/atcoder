n, k = map(int, input().split())
h = list(map(int, input().split()))

INF = 10 ** 10
dp = [INF] * 100100

dp[0] = 0
for i in range(n):
    j = 1
    while j <= k and i + j < n:
        dp[i + j] = min(dp[i + j], dp[i] + abs(h[i + j] - h[i]))
        j += 1

print(dp[n - 1])