# |V|が頂点数、|E|が辺数のとき　計算量はO(|V| + |E|)

n, m = map(int, input().split())

g = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

seen = [False] * n

def dfs(v):
    seen[v] = True

    for next_v in g[v]:
        if not seen[next_v]: dfs(next_v)

dfs(0)