# result: https://atcoder.jp/contests/abc129/submissions/7235293

n, m = list(map(int,input().split()))
issafe = [True] * (n + 1)

for i in range(m):
    a = int(input())
    issafe[a] = False

dp = [0] * (n + 1)

dp[0] = 1
if issafe[1]: dp[1] = 1;

for i in range(n - 1):
    if issafe[i]: dp[i + 2] += dp[i]
    if issafe[i + 1]: dp[i + 2] += dp[i + 1]
    dp[i + 2] %= 1000000007

print(dp[n])
