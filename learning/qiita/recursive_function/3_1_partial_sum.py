n = int(input())
a = [int(input()) for _ in range(n)]
x = int(input())

def solve(i, sum):
    if i == n:
        if sum == 0:
            return True
        else:
            return False
    
    if solve(i + 1, sum):
        return True
    
    if solve(i + 1, sum - a[i]):
        return True
    
    return False

if solve(0, x):
    print("Yes")
else:
    print("No")