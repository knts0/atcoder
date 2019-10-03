n, m = map(int, input().split())
g = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

nodes = 0
edges = 0
seen = [False] * n

def dfs(v, prev):
    seen[v] = True
    
    ok = True
    for next_v in g[v]:
        if seen[next_v] and next_v != prev:
            return False
        if not seen[next_v]: 
            if not dfs(next_v, v):
                ok = False
    return ok

ans = 0
for i in range(n):
    if not seen[i]:
        if dfs(i, -1):
            ans += 1

print(ans)