n, w = map(int, input().split())
ws = [0] * n
vs = [0] * n
for i in range(n):
    ww, vv = map(int, input().split())
    ws[i] = ww
    vs[i] = vv

dp = [[0] * (w + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(w + 1):
        if j - ws[i] >= 0:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - ws[i]] + vs[i])
        
        dp[i + 1][j] =  max(dp[i + 1][j], dp[i][j])

print(dp[n][w])
        