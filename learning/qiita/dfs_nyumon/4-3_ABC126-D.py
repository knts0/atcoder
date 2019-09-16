# result: https://atcoder.jp/contests/abc126/submissions/7567067

n = int(input())

g = [[] for _ in range(n)]
for i in range(n - 1):
    u, v, w = map(int, input().split())
    g[u - 1].append((v - 1, w))
    g[v - 1].append((u - 1, w))

color = [-1] * n
dist = [0] * n

import queue
def dfs(v):
    color[v] = dist[v] % 2
    q = queue.LifoQueue()
    q.put(v)

    while not q.empty():
        vv = q.get()
        for next_v in g[vv]:
            if color[next_v[0]] == -1 and next_v[1] != 0:
                dist[next_v[0]] = dist[vv] + next_v[1]
                color[next_v[0]] = dist[next_v[0]] % 2
                q.put(next_v[0])

# 0を始点として各点までの距離を求める
dfs(0)

for c in color:
    print(c)