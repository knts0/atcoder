n = int(input())
a = [int(input()) for _ in range(n)]
x = int(input())

MAX = 100000
dp = [[-1] * MAX for _ in range(n + 1)]

def solve(i, sum):
    if i == n:
        if sum == 0:
            return 1
        else:
            return 0
    
    if sum < 0:
        return 0

    if dp[i][sum] != -1:
        dp[i][sum] = 1
        return 1
    
    if solve(i + 1, sum):
        dp[i][sum] = 1
        return 1
    
    if solve(i + 1, sum - a[i]):
        dp[i][sum] = 1
        return 1
    
    dp[i][sum] = 0
    return 0

if solve(0, x):
    print("Yes")
else:
    print("No")