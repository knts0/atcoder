import sys
import math

a = []
while True:
    n = int(input())
    if n == 0:
        break
    a.append(n)

for n in a:
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n + 1):
        if i > 0: dp[i] += dp[i - 1]
        if i > 1: dp[i] += dp[i - 2]
        if i > 2: dp[i] += dp[i - 3]
    
    print(int(math.ceil(dp[n] / (365 * 10))))