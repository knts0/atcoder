# result: http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=3894240#2

n = int(input())
a = list(map(int, input().split()))

dp = [[0 for _ in range(1100)] for _ in range(110)]

last = a[-1]

dp[0][0] = 1

for i in range(n):
    for j in range(100):
        if i == 0:
            dp[i + 1][a[i]] = 1

        # +
        if 0 <= j + a[i] <= 20:
            dp[i + 1][j + a[i]] += dp[i][j]
        # -
        if 0 <= j - a[i] <= 20:
            dp[i + 1][j - a[i]] += dp[i][j]

print(dp[n - 1][last])