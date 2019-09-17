# トポロジカルソート
n, m = map(int, input().split())

g = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)

seen = [False] * n
order = []

import queue
def dfs(v):
    seen[v] = True
    for next_v in g[v]:
        if seen[next_v]:
            continue
        dfs(next_v)
    order.append(v)

for v in range(n):
    if seen[v]: continue
    dfs(v)

order.reverse()