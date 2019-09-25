# result: https://arc057.contest.atcoder.jp/submissions/7696058

n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

INF = 10 ** 9 + 100
dp = [[INF] * 2010 for _ in range(2010)]

dp[0][0] = 0
sum = 0
for i in range(n):
    if i == 0:
        dp[1][1] = 1
        dp[1][0] = 0
    else:
        for j in range(i + 1):
            if dp[i][j] < INF:
                y = dp[i][j] * a[i]
                y = y // sum + 1
                if y <= a[i]:
                    dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + y)
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
    
    sum += a[i]

if sum == 0:
    print(0)
elif sum == k:
    print(1)
else:
    check = False
    for i in range(n, 0, -1):
        if dp[n][i] <= k:
            print(i)
            check = True
            break
    if not check:
        print(0)