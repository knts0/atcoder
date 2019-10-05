# ダイクストラ法
# |V|が頂点数、|E|が辺数のとき　計算量はO(|E|log|v|)

n, m = map(int, input().split())

g = [[] for _ in range(n)]

for i in range(m):
    a, b, w = map(int, input().split())
    g[a - 1].append({ 'to': b - 1, 'weight': w })
    g[b - 1].append({ 'to': a - 1, 'weight': w })

INF = 10 ** 9
dist = [INF] * n  # 最短距離

import heapq
def dijkstra(s):
    q = []
    heapq.heapify(q)

    dist[s] = 0
    heapq.heappush({ 'd': 0, 'v': s })

    while len(q) > 0:
        p = heapq.heappop(q)

        if dist[p.v] < p.d:
            continue

        for next_p in g[p.v]:
            if dist[next_p.v] > dist[p.v] + next_p.w:
                dist[next_p.v] = dist[p.v] + next_p.w
                heapq.heappush((dist[next_p.v], next_p.v))
