# Breadth First Search

visited = [False] * 100
d = [0] * 100

import queue
def bfs():
    q = queue.Queue()
    q.put(0)

    while not q.empty():
        u = q.get()

        for v in graph[u]:
            if not visited[v]:
                q.put(v)
                d[v] = d[u] + 1
                visited[v] = True

n = int(input())

graph = [[] for i in range(n)]
for i in range(n):
    lst = list(map(int,input().split()))

    if lst[1] > 0:
        u = lst[0]
        for v in lst[2:]:
            graph[u - 1].append(v - 1) # 0-originにする

bfs()

for u in range(n):
    print(str(u + 1) + " " + str(d[u]))