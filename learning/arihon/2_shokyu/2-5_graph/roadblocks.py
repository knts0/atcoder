n, r = map(int, input().split())

g = [[] for i in range(n)]
for i in range(r):
    a, b, d = map(int, input().split())
    g[a - 1].append((b - 1, d))
    g[b - 1].append((a - 1, d))

INF = 10 ** 9
dist = [INF] * n
dist2 = [INF] * n

import heapq
q = []
heapq.heapify(q)

d[0] = 0
heapq.heappush(q, (0, 0))

while len(q) > 0:
    p = heapq.heappop
    idx = p[1]
    d = p[0]

    if dist2[idx] < d:
        continue

    for nv in g[idx]:
        nv_idx = nv[0]
        nv_d = nv[1]

        d2 = d + nv_d

        if dist[nv_idx] > d2:
            dist[nv_idx], d2 = d2, dist[nv_idx]
            heapq.heappush((dist[nv_idx], nv_idx))
        
        if dist2[nv_idx] > d2 and dist[nv_idx] < d2:
            dist2[nv_idx] = d2
            heapq.heappush((dist2[nv_idx], nv_idx))

print(dist2[n - 1])