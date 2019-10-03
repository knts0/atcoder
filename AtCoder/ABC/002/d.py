# result: https://atcoder.jp/contests/abc002/submissions/7839239

n, m = map(int, input().split())

g = [[False] * n for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    g[a - 1][b - 1] = True

ans = 0
for bit in range(2 ** n):
    ok = True
    cnt = 0
    for i in range(n):
        if bit >> i & 1:
            cnt += 1
        for j in range(n):
            if bit >> i & 1 and bit >> j & 1 and i < j and not g[i][j]:
                ok = False
    
    if ok:
        ans = max(ans, cnt)

print(ans)