# result: https://tdpc.contest.atcoder.jp/submissions/7672187

n = int(input())
p = list(map(int, input().split()))

dp = [[False] * 10010 for _ in range(n + 1)]
dp[0][0] = True
for i in range(n):
    for j in range(10010):
        if dp[i][j]:
            dp[i + 1][j + p[i]] = True
            dp[i + 1][j] = True

ans = 0
for i in range(10010):
    if dp[n][i]:
        ans += 1

print(ans)