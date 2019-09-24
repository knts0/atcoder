# result: https://atcoder.jp/contests/dp/submissions/7684424

n, w = map(int, input().split())
ws = [0] * n
vs = [0] * n

for i in range(n):
    ws[i], vs[i] = map(int, input().split())

INF = 10 ** 18
dp = [[INF] * 100010 for _ in range(110)]
dp[0][0] = 0
for i in range(n):
    for sum_v in range(100010):
        # i番目を選ぶ
        if sum_v - vs[i] >= 0:
            dp[i + 1][sum_v] = min(dp[i + 1][sum_v], dp[i][sum_v - vs[i]] + ws[i])
        
        # i番目を選ばない
        dp[i + 1][sum_v] = min(dp[i + 1][sum_v], dp[i][sum_v])

ans = 0
for sum_v in range(100010):
    if dp[n][sum_v] <= w:
        ans = sum_v

print(ans)