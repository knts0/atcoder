# result: https://atcoder.jp/contests/maximum-cup-2018/submissions/7803497

n = int(input())

g = [[] for _ in range(n)]

for i in range(n):
    a = int(input())
    g[i].append(a - 1)

color = [-1] * n

cnt = [0] * 2

def dfs(v, c):
    color[v] = c
    cnt[c] += 1

    for next_v in g[v]:
        if color[next_v] == c:
            return False

        if color[next_v] == -1: 
            if not dfs(next_v, 1 - c):
                return False
    return True

ok = True
ans = 0
for i in range(n):
    if color[i] != -1:
        continue
    if dfs(i, 0):
        ans += max(cnt)
        cnt = [0] * 2
    else:
        ok = False

if ok:
    print(ans)
else:
    print(-1)