n, m, s, t = map(int, input().split())

g = [[] for _ in range(n)]

for i in range(m):
    u, v, a, b = map(int, input().split())
    g[u - 1].append({ 'to': v - 1, 'a': a, 'b': b })
    g[v - 1].append({ 'to': u - 1, 'a': a, 'b': b })

INF = 10 ** 17
dist = [[INF] * (n + 1) for _ in range(n + 1)]


import heapq
def dijkstra(s):
    q1 = []
    q2 = []
    heapq.heapify(q1)
    heapq.heapify(q2)

    dist[s] = 0
    heapq.heappush(q1, { 'd': 0, 'v': 0 })
    heapq.heappush(q2, { 'd': 0, 'v': s + 1})

    while len(q1) > 0 or len(q2) > 0:
        p1 = heapq.heappop(q1)
        p2 = heapq.heappop(q2)

        if dist[p1.v][0] < p1.d:
            continue

        if dist[p2.v][p2.v + 1] < p2.d:
            continue

        for next_p in g[v]:

            if dist[next_p.v][0] > dist[p1.v][0] + next_p.a:
                dist[next_p.v][0] = dist[p1.v][0] + next_p.a
                heapq.heappush(q1, (dist[next_p.v][0], next_p.v))
            
            if dist[next_p.v][p2.v + 1] > dist[p2.v][0] + next_p.b:
                dist[next_p.v][p2.v + 1] = dist[p2.v][0] + next_p.b
                heapq.heappush(q1, (dist[next_p.v][p2.v + 1], next_p.v))