# ダイクストラ法
# |V|が頂点数、|E|が辺数のとき　計算量はO(|E|log|v|)

n, m = map(int, input().split())

g = [[] for _ in range(n)]

for i in range(m):
    a, b, w = map(int, input().split())
    g[a - 1].append((b - 1, w))
    g[b - 1].append((a - 1, w))

INF = 10 ** 9
dist = [INF] * n  # 最短距離
prev = [-1] * n # 最短経路における各頂点の直前の頂点

import heapq
def dijkstra(s):
    q = []
    heapq.heapify(q)

    dist[s] = 0
    heapq.heappush((0, s))

    while len(q) > 0:
        p = heapq.heappop(q)
        v = p[1]

        if dist[v] < p[0]:
            continue

        for next_p in g[v]:
            next_v = next_p[0]
            e = next_p[1]

            if dist[next_v] > dist[v] + e:
                dist[next_v] = dist[v] + e
                prev[next_v] = v
                heapq.heappush((dist[next_v], next_v))

def restore_route(t):
    path = []
    while t != -1:
        path.append(t)
        t = prev[t]
    return reversed(path)