# result: https://tdpc.contest.atcoder.jp/submissions/7672444

import sys

n, d = map(int, input().split())

def prime_factorization(num):
    two = 0
    while num % 2 == 0:
        two += 1
        num /= 2
    three = 0
    while num % 3 == 0:
        three += 1
        num /= 3
    five = 0
    while num % 5 == 0:
        five += 1
        num /= 5
    ok = True if num == 1 else False
    return (two, three, five, ok)
(two, three, five, ok) = prime_factorization(d)
if not ok:
    print(0)
    sys.exit()

dp = [[[[0] * (five + 1) for _ in range(three + 1)] for _ in range(two + 1)] for _ in range(n + 1)]

dp[0][0][0][0] = 1.0
for i in range(n):
    for pc2 in range(two + 1):
        for pc3 in range(three + 1):
            for pc5 in range(five + 1):
                j = 1
                while j <= 6:
                    nc2 = min(two, pc2 + 1 if j == 2 or j == 6 else pc2 + 2 if j == 4 else pc2)
                    nc3 = min(three, pc3 + 1 if j == 3 or j == 6 else pc3)
                    nc5 = min(five, pc5 + 1 if j == 5 else pc5)
                    dp[i + 1][nc2][nc3][nc5] += dp[i][pc2][pc3][pc5]/6.0
                    j += 1

print(dp[n][two][three][five])