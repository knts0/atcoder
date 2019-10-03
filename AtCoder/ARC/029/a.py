n = int(input())
t = [int(input()) for _ in range(n)]

ans = 10 ** 9
for i in range(2 ** n):
    cnt1 = 0
    cnt2 = 0
    for j in range(n):
        if i >> j & 1:
            cnt1 += t[j]
        else:
            cnt2 += t[j]
    
    ans = min(ans, max(cnt1, cnt2))

print(ans)