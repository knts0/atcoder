# |V|が頂点数、|E|が辺数のとき　計算量はO(|V| + |E|)

n, m = map(int, input().split())

g = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

dist = [-1] * n  # 最短距離

import queue
def bfs(u):
    q = queue.Queue()
    dist[u] = 0
    q.put(u)

    while not q.empty():
        v = q.get()
        for next_v in g[v]:
            if dist[next_v] == -1:
                q.put(next_v)
                dist[next_v] = dist[v] + 1
