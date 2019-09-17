# 木上のDFS
n = int(input())

g = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

dist = [0] * n

import queue
def dfs(v, p):
    q = queue.LifoQueue()
    q.put(v)

    while not q.empty():
        vv = q.get()
        for next_v in g[vv]:
            if next_v == p:
                continue
            q.put(next_v)

# 0を始点とする（親は-1）
dfs(0, -1)