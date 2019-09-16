# |V|が頂点数、|E|が辺数のとき　計算量はO(|V| + |E|)

n, m = map(int, input().split())

g = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

seen = [False] * n

ans = 0
def dfs(v):
    seen[v] = True

    for next_v in g[v]:
        if not seen[next_v]: dfs(next_v)

for v in range(n):
    if not seen[v]:
        dfs(v)
        ans += 1

print(ans)