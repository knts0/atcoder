# 最小全域木を求める
n, m = map(int, input().split())

MAX_V = 10 ** 5
INF = 10 ** 9
d = [[INF] * MAX_V for _ in range(MAX_V)]
mincost = [INF] * MAX_V
used = [False] * MAX_V

for i in range(m):
    a, b, w = map(int, input().split())
    d[a - 1][b - 1] = w
    d[b - 1][a - 1] = w

import heapq
def prim():
    mincost[0] = 0
    res = 0

    q = []
    heapq.heapify(q)
    heapq.heappush((0, 0))

    while len(q) > 0:
        p = heapq.heappop(q)
        v = p[1]

        used[v] = True
        res += mincost[v]

        new_q = []
        heapq.heapify(new_q)

        for next_p in range(n):
            if d[v][next_p] != INF and not used[next_p]:
                mincost[next_p] = min(mincost[next_p], d[v][next_p])
                heapq.heappush((mincost[next_p], next_p))
        
        q, new_q = new_q, q