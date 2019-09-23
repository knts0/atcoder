n = int(input())

INF = 100010
dp = [INF] * (n + 1)
dp[0] = 0
for i in range(n + 1):
    if i + 1 <= n: dp[i + 1] = min(dp[i + 1], dp[i] + 1)
    
    j = 6
    while i + j <= n:
        dp[i + j] = min(dp[i + j], dp[i] + 1)
        j *= 6
    
    j = 9
    while i + j <= n:
        dp[i + j] = min(dp[i + j], dp[i] + 1)
        j *= 9

print(dp[n])