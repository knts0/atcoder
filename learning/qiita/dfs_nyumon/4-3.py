# |V|が頂点数、|E|が辺数のとき　計算量はO(|V| + |E|)

n, m = map(int, input().split())

g = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

color = [-1] * n

is_bipartite = True
def dfs(v, cur = 0):
    color[v] = cur

    for next_v in g[v]:
        if color[next_v] != -1:
            if color[next_v] == cur:
                return False
                continue
        
        if not dfs(next_v, 1 - cur):
            return False
    
    return True

for v in range(n):
    if color[v] == -1:
        if not dfs(v):
            is_bipartite = False

if is_bipartite:
    print("Yes")
else:
    print("No")